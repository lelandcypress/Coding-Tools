import subprocess

def tail(filename):
    process = subprocess.Popen(['tail', '-F', filename], stdout=subprocess.PIPE)

    while True:
        line = process.stdout.readline()

        if not line:
            process.terminate()
            return

        yield line
