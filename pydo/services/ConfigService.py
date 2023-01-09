import dataclasses
from pathlib import Path

import orjson

from pydo.config.Config import Config
from pydo.config.LoggerConfig import LoggerConfig
from pydo.config.ModuleConfig import ModuleConfig
from pydo.services.interfaces.IConfigService import IConfigService
from pydo.utilities.WithLogging import WithLogging


@dataclasses.dataclass
class ConfigService(IConfigService):
    config: dict
    config_file_path: Path
    config_dir_path: Path
    config_service: IConfigService

    def __init__(self, config_path: Path):
        super().__init__()
        self.config_file_path = config_path
        self.config_dir_path = config_path.parent
        self.config = Config.load(config_path)

        logger_config = self.get_logger_config()
        WithLogging.initialize_logger(logger_config)

    def get_config_path(self, name: str, config_dir: str = None) -> Path:
        config_path_stem = Path(config_dir) / name if config_dir else name
        return (self.config_dir_path / config_path_stem).with_suffix(".json")

    def get_config(self, name: str, config_dir: str = None, config_class=None) -> Config:
        path: Path = self.get_config_path(name, config_dir)
        if not path.exists():
            for parent in path.parents:
                parent.mkdir(parents=True, exist_ok=True)
            path.touch()
            with open(path, "w") as file:
                file.write("{}")
        return Config.load(path, config_class)

    def save_config(self, config: Config, instance_name: str, config_dir: str = None) -> None:
        data = orjson.dumps(config, orjson.OPT_INDENT_2)
        path: Path = self.get_config_path(instance_name)
        writer = open(path, "w")
        writer.write(data.decode("utf-8"))
        writer.close()

    @staticmethod
    def get_config_class(config: dict, name: str):
        try:
            class_name = config["type"] + "Config"
        except KeyError:
            class_name = name

        config_module = __import__(f"pydo.config.{class_name}", fromlist=[class_name])
        return getattr(config_module, class_name)

    def get_enabled_modules(self) -> list[str]:
        return self.config["enabled_modules"]

    def get_logger_config(self) -> LoggerConfig:
        return self.get_config("LoggerConfig", config_class=LoggerConfig)

    def get_modules_dir(self) -> Path:
        return self.config_dir_path / "modules"

    def get_config_from_file(self, file_path: str) -> Config:
        with open(file_path, "r") as file:
            config = orjson.loads(file.read())
            config_class = self.get_config_class(config, file_path)
            return config_class(config)

    def get_module_config(self, data: dict) -> ModuleConfig:
        config_class = self.get_config_class(data, data["name"])
        return config_class(data)
