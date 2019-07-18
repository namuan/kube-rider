from typing import List

import attr


@attr.s(auto_attribs=True)
class AppState:
    contexts: List[str] = []
    commands: List[str] = []
