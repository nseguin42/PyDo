import threading
import uuid
from abc import ABCMeta, abstractmethod
from pathlib import Path
from typing import Self, Set
from uuid import UUID

from pydo.config.interfaces.IConfigurable import IConfigurable
from pydo.config.TaskConfig import TaskConfig
from pydo.utilities.ClassLoader import get_task_class
from pydo.utilities.WithLogging import WithLogging


class Task(IConfigurable, WithLogging, metaclass=ABCMeta):
    name: str
    aliases: Set[str]
    config: TaskConfig
    dependencies: Set[Self] = set()
    lock: threading.Lock
    _id: UUID

    @abstractmethod
    def __init__(self,
                 config: TaskConfig):
        super().__init__(config)
        self.name = config.name
        self._id = uuid.uuid4()
        self.aliases = config.aliases

    @staticmethod
    def load(config: TaskConfig):
        if config.type:
            task_class = get_task_class(config.type)
            return task_class(config)
        else:
            raise Exception("Task type not specified")

    @staticmethod
    def load_from_file(path: Path):
        task = Task.load(path)
        return task

    def run(self):
        pass

    def get_short_id(self):
        return self._id.hex[:8]

    def __repr__(self):
        return "Task: " + self.name + " (" + str(self.get_short_id() + ")")

    def __eq__(self, other):
        return self._id == other._id

    def __hash__(self):
        return hash(self._id)
