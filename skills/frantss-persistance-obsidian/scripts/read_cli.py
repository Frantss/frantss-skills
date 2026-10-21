import subprocess
import sys
import tempfile
with tempfile.TemporaryFile() as output, tempfile.TemporaryFile() as errors:
    result = subprocess.run(["obsidian", *sys.argv[1:]], stdin=subprocess.DEVNULL, stdout=output, stderr=errors, timeout=15)
    for source, target in [(output, sys.stdout.buffer), (errors, sys.stderr.buffer)]:
        source.seek(0)
        target.write(source.read())
sys.exit(result.returncode)
