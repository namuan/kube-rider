import subprocess
import time


class ConsoleManager:
    abort_long_running_command = False

    def run_command(self, command):
        return subprocess.check_output(
            command,
            stderr=subprocess.STDOUT,
            shell=True
        ).decode('utf-8')

    def run_long_running_command(self, command):
        p = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True
        )

        while not self.abort_long_running_command:
            p.poll()
            line = p.stdout.readline()
            yield line
            time.sleep(1)
