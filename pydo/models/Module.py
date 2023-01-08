import logging
import threading
import uuid
from abc import ABCMeta, abstractmethod
from typing import Self, Set
from uuid import UUID

from pydo.config.interfaces.IConfigurable import IConfigurable
from pydo.config.ModuleConfig import ModuleConfig
from pydo.services.interfaces.WithLogging import WithLogging


class Module(IConfigurable, WithLogging, metaclass=ABCMeta):
    config: ModuleConfig
    dependencies: Set[Self] = set()
    lock: threading.Lock
    _id: UUID

    @abstractmethod
    def __init__(self,
                 instance_name: str,
                 config: ModuleConfig):
        super().__init__(config, instance_name)
        self._id = uuid.uuid4()
        self.lock = threading.Lock()

    def run(self):
        pass

    def get_short_id(self):
        return self._id.hex[:8]

    def __repr__(self):
        return "Module: " + self.instance_name + " (" + str(self.get_short_id() + ")")

    def __eq__(self, other):
        return self._id == other._id

    def __hash__(self):
        return hash(self._id)

