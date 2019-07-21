import subprocess


class ConsoleManager:

    def run_command(self, command):
        return subprocess.check_output(
            command,
            stderr=subprocess.STDOUT,
            shell=True
        ).decode('utf-8')
