import logging
import subprocess
import time
from pathlib import Path

command_file_mapping = {
    "kubectl config get-contexts --output='name'": "k_get_contexts.txt",
    "kubectl config current-context": "k_get_current_context.txt",
    "kubectl --context qa get namespaces -o json": "k_get_qa_namespaces.json",
    "kubectl --context development get namespaces -o json": "k_get_test_namespaces.json",
    "kubectl --context test get namespaces -o json": "k_get_test_namespaces.json",
    "kubectl --context qa --namespace default get pods -o json": "k_get_qa_multiple_pods.json",
    "kubectl --context qa --namespace kube-public get pods -o json": "k_get_qa_single_pod.json",
    "kubectl --context qa --namespace default get event --field-selector='involvedObject.name=hello-node-2-7c99ff6cd7-gtpxr' -o json": "k_get_pod_events.json"
}


class MockConsoleManager:
    abort_long_running_command = False

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

    def run_long_running_command(self, command):
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

        while not self.abort_long_running_command:
            ret_code = p.poll()
            line = p.stdout.readline()
            yield line
            time.sleep(1)
            if ret_code is not None or ret_code is not 0:
                break
