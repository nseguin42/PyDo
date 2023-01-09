import dataclasses


@dataclasses.dataclass
class Script:
    script: str
    lang: str
    interactive: bool

    def __init__(self, dict: dict):
        self.script = dict["script"]
        self.lang = dict["lang"]
        self.interactive = dict["interactive"] if "interactive" in dict else False
