from pathlib import Path

from pydo.config.Config import Config
from pydo.services.interfaces.IConfigService import IConfigService
from pydo.services.interfaces.IConfigurableService import IConfigurableService
from pydo.tasks.Task import Task


class TaskLoaderService(IConfigurableService):
    tasks: list[Task] = []

    def __init__(self, config_service: IConfigService):
        super().__init__(config_service)

    def load_tasks(self) -> list[Task]:
        task_dir = Path(self.config_service.get_tasks_dir())
        for task_path in task_dir.iterdir():
            if not task_path.is_file():
                continue
            task = self.load_task_from_config(task_path)
            self.tasks.append(task)

        self.register_dependencies()
        return self.tasks

    def load_task_from_config(self, config_file_path: Path) -> Task:
        task_config = Config.load(config_file_path)
        return Task.load(task_config)

    def register_dependencies(self):
        for task in self.tasks:
            task.dependencies = {tasks for tasks in self.tasks if
                                 tasks.name in task.config.get_dependencies()}
