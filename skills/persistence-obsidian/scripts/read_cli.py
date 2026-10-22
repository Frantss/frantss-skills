import subprocess
import sys
import tempfile


def run_cli(arguments):
    with tempfile.TemporaryFile() as output, tempfile.TemporaryFile() as errors:
        result = subprocess.run(["obsidian", *arguments], stdin=subprocess.DEVNULL,
                                stdout=output, stderr=errors, timeout=5)
        output.seek(0)
        errors.seek(0)
        return subprocess.CompletedProcess(result.args, result.returncode, output.read(), errors.read())


if __name__ == "__main__":
    result = run_cli(sys.argv[1:])
    sys.stdout.buffer.write(result.stdout)
    sys.stderr.buffer.write(result.stderr)
    sys.exit(result.returncode)
