import threading
import uuid
from abc import ABCMeta, abstractmethod
from modulefinder import Module
from typing import Self, Set
from uuid import UUID

from pydo.config.interfaces.IConfigurable import IConfigurable
from pydo.config.ModuleConfig import ModuleConfig
from pydo.utilities.WithLogging import WithLogging


def get_class(name: str):
    if name:
        module = __import__(f"pydo.modules.{name}", fromlist=[name])
        return getattr(module, name)


class Module(IConfigurable, WithLogging, metaclass=ABCMeta):
    name: str
    config: ModuleConfig
    dependencies: Set[Self] = set()
    lock: threading.Lock
    _id: UUID

    @abstractmethod
    def __init__(self,
                 config: ModuleConfig):
        super().__init__(config)
        self.name = config.name
        self._id = uuid.uuid4()

    @staticmethod
    def load(config: ModuleConfig) -> Module:
        if config.type:
            module_class = get_class(config.type)
            return module_class(config)
        else:
            raise Exception("Module type not specified")

    def run(self):
        pass

    def get_short_id(self):
        return self._id.hex[:8]

    def __repr__(self):
        return "Module: " + self.name + " (" + str(self.get_short_id() + ")")

    def __eq__(self, other):
        return self._id == other._id

    def __hash__(self):
        return hash(self._id)
