from typing import List

import attr


@attr.s(auto_attribs=True)
class AppState:
    contexts: List[str] = []
    commands: List[str] = []
    current_context: str = None
    namespaces: List[str] = []
    current_namespace: str = None
