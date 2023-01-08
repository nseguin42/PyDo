from abc import ABCMeta


class Config(metaclass=ABCMeta):
    type: str
    config: dict
    config_dir: str = ""

    def __init__(self, config: dict):
        try:
            self.type = config["type"]
            self.config = config["config"]
        except KeyError:
            self.config = config
