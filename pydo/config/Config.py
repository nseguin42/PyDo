import json
from abc import ABCMeta
from pathlib import Path

from pydo.utilities.ClassLoader import get_module_config_class


class Config(metaclass=ABCMeta):
    config: dict
    path: Path
    type: str
    name: str

    def __init__(self, config: dict):
        if "type" in config:
            self.type = config["type"]
        if "name" in config:
            self.name = config["name"]
        if "config" in config:
            self.config = config["config"]
        else:
            self.config = config

    @staticmethod
    def load(path: Path, config_class=None):
        with open(path, "r") as file:
            dict = json.loads(file.read())
            if "type" in dict:
                config_class = get_module_config_class(dict["type"])

            if config_class is None:
                config = Config(dict)
            else:
                config = config_class(dict)
            config.path = path
            return config

    def save(self):
        with open(self.path, "w") as file:
            json.dump(self.config, file, indent=4)

    def get_property(self, name: str, default_value: str = None):
        if default_value:
            return self.get_optional_property(name, default_value)
        else:
            return self.get_required_property(name)

    def get_required_property(self, name: str):
        try:
            return self.config[name]
        except KeyError:
            raise KeyError("Required property " + name + " not found in config" + str(self.config))

    def get_optional_property(self, name: str, default_value):
        try:
            return self.config[name]
        except KeyError:
            return default_value
