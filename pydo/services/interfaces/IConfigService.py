from abc import ABCMeta, abstractmethod
from pathlib import Path

from pydo.config.Config import Config
from pydo.config.LoggerConfig import LoggerConfig
from pydo.config.TaskConfig import TaskConfig
from pydo.services.interfaces.IService import IService


class IConfigService(IService, metaclass=ABCMeta):

    @abstractmethod
    def get_config(self, instance_name: str) -> Config:
        pass

    @abstractmethod
    def save_config(self, config: Config, instance_name: str, config_dir: str = None) -> None:
        pass

    @abstractmethod
    def get_tasks_dir(self) -> Path:
        pass

    @abstractmethod
    def get_task_config(self, data: dict) -> TaskConfig:
        pass

    @abstractmethod
    def get_enabled_tasks(self) -> list[str]:
        pass

    @abstractmethod
    def get_logger_config(self) -> LoggerConfig:
        pass
