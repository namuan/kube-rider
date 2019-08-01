import logging
import time
from pathlib import Path

command_file_mapping = {
    "kubectl config get-contexts --output='name'": "k_get_contexts.txt",
    "kubectl config current-context": "k_get_current_context.txt",
    "kubectl --context qa get namespaces -o json": "k_get_qa_namespaces.json",
    "kubectl --context development get namespaces -o json": "k_get_test_namespaces.json",
    "kubectl --context test get namespaces -o json": "k_get_test_namespaces.json",
    "kubectl --context qa --namespace default get pods -o json": "k_get_qa_multiple_pods.json",
    "kubectl --context qa --namespace kube-public get pods -o json": "k_get_qa_single_pod.json"
}


class MockConsoleManager:
    def __init__(self):
        self.mock_responses_dir = Path(".").joinpath("mock_responses")

    def run_command(self, command):
        logging.debug(f"Running command: {command}")
        mock_repsonse = command_file_mapping.get(command, None)
        if mock_repsonse:
            time.sleep(0.1)
            return self.mock_responses_dir.joinpath(mock_repsonse).read_text()
        else:
            raise LookupError(f"No Mock found for command: {command}")
