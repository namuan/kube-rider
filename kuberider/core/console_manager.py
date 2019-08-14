import logging
import subprocess
import time

from kuberider.core.terminal import Terminal


class ConsoleManager:
    abort_long_running_command = False
    terminal = Terminal()

    def run_command(self, command):
        logging.debug(f"Running command: {command}")
        return subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True).decode('utf-8')

    def run_long_running_command(self, command):
        p = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True
        )

        while not self.abort_long_running_command:
            ret_code = p.poll()
            line = p.stdout.readline()
            yield line
            time.sleep(0.2)
            if ret_code is not None or ret_code is not 0:
                break

    def run_osx_terminal(self, command):
        return self.terminal.open_terminal(script=command)
