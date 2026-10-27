import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "skills/obsidian/scripts/read_cli.py"


@unittest.skipUnless(os.name == "posix", "CLI fixture uses a POSIX executable")
class ObsidianReadCliTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.bin = Path(self.directory.name)
        self.env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PATH=str(self.bin) + os.pathsep + os.environ.get("PATH", ""))

    def run_cli(self, source, *arguments):
        executable = self.bin / "obsidian"
        executable.write_text("#!" + sys.executable + "\n" + source)
        executable.chmod(0o700)
        process = subprocess.Popen(
            [sys.executable, str(SCRIPT), *arguments], env=self.env,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
            start_new_session=True,
        )
        try:
            stdout, stderr = process.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            stdout, stderr = process.communicate()
            self.fail("CLI remained running after returning output: " + repr(stdout))
        finally:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        return process.returncode, stdout, stderr

    def test_preserves_arguments_and_multiline_output(self):
        arguments = ["vault=Example vault", "read", "path=Folder/Note with spaces.md"]
        code, stdout, stderr = self.run_cli(
            "import sys,json\nprint(json.dumps(sys.argv[1:]))\nprint('line 1\\nline 2: café')\n",
            *arguments,
        )
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(stdout.splitlines()[0]), arguments)
        self.assertEqual(stdout.splitlines()[1:], ["line 1", "line 2: café"])
        self.assertEqual(stderr, "")

    def test_import_does_not_run_the_cli(self):
        result = subprocess.run(
            [sys.executable, '-c',
             'import sys; sys.path.insert(0, sys.argv[1]); from read_cli import run_cli; print("imported")',
             str(SCRIPT.parent)], env=self.env, capture_output=True, text=True, timeout=10,
        )
        self.assertEqual((result.returncode, result.stdout, result.stderr), (0, 'imported\n', ''))

    def test_preserves_failure_status_and_stderr(self):
        code, stdout, stderr = self.run_cli(
            "import sys\nprint('synthetic failure',file=sys.stderr)\nsys.exit(7)\n", "read",
        )
        self.assertEqual((code, stdout, stderr), (7, "", "synthetic failure\n"))

    def test_descendant_holding_stdout_does_not_block_completion(self):
        code, stdout, stderr = self.run_cli(
            "import subprocess,sys\n"
            "subprocess.Popen([sys.executable,'-c','import time; time.sleep(60)'])\n"
            "print('complete synthetic note')\n", "read",
        )
        self.assertEqual((code, stdout, stderr), (0, "complete synthetic note\n", ""))

    def test_output_without_exit_is_not_a_successful_read(self):
        code, stdout, stderr = self.run_cli(
            "import time\nprint('synthetic note content',flush=True)\ntime.sleep(60)\n", "read",
        )
        self.assertNotEqual(code, 0)
        self.assertEqual(stdout, "")
        self.assertIn("TimeoutExpired", stderr)
