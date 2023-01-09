from abc import ABCMeta, abstractmethod
from typing import List

from tasks.Task import Task
from pydo.services.interfaces.IConfigurableService import IConfigurableService


class ITaskRunnerService(IConfigurableService, metaclass=ABCMeta):
    @abstractmethod
    def run(self, task: Task):
        pass

    def run_all(self, tasks: List[Task]):
        for task in tasks:
            self.run(task)
