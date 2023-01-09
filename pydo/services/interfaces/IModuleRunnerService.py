from abc import ABCMeta, abstractmethod
from typing import List

from modules.Module import Module
from pydo.services.interfaces.IConfigurableService import IConfigurableService


class IModuleRunnerService(IConfigurableService, metaclass=ABCMeta):
    @abstractmethod
    def run(self, module: Module):
        pass

    def run_all(self, modules: List[Module]):
        for module in modules:
            self.run(module)
