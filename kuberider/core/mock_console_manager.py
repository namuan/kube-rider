from pathlib import Path


class MockConsoleManager:
    def __init__(self):
        self.mock_responses_dir = Path(".").joinpath("mock_responses")

    def run_command(self, command):
        mock_file = self.mock_responses_dir.joinpath("k_get_contexts.txt").read_text()
        return mock_file
