from abc import ABCMeta, abstractmethod
from typing import List

from pydo.services.interfaces.IConfigurableService import IConfigurableService
from tasks.Task import Task


class ITaskRunnerService(IConfigurableService, metaclass=ABCMeta):
    @abstractmethod
    def run(self, task: Task):
        pass

    def run_all(self, tasks: List[Task]):
        for task in tasks:
            self.run(task)
