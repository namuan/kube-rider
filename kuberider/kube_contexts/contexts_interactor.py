import logging

from kuberider.core.worker_pool import CommandThread


class KubeContextsLoader:
    def __init__(self):
        self.ct = CommandThread()

    def load_contexts(self):
        command = "kubectl config get-contexts --output='name'"
        self.ct.command = command
        self.ct.signals.success.connect(self.on_result)
        self.ct.signals.failure.connect(self.on_result)
        self.ct.start()

    def on_result(self, result):
        logging.info(f"Result from command: {result['command']} => {result['status']}")
        logging.info(f"Output: {result['output']}")
