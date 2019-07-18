import logging
from pathlib import Path

command_file_mapping = {
    "kubectl config get-contexts --output='name'": "k_get_contexts.txt",
    "kubectl config current-contexts": "k_get_current_context.txt"
}


class MockConsoleManager:
    def __init__(self):
        self.mock_responses_dir = Path(".").joinpath("mock_responses")

    def run_command(self, command):
        logging.debug(f"Running command: {command}")
        mock_repsonse = command_file_mapping.get(command, None)
        if mock_repsonse:
            return self.mock_responses_dir.joinpath(mock_repsonse).read_text()
        else:
            return f"No Mock found for command: {command}"
