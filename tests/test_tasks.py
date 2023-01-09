import unittest
from pathlib import Path

from pydo.config.LoggerConfig import LoggerConfig
from pydo.config.TaskConfig import TaskConfig
from pydo.services.ConfigService import ConfigService
from pydo.services.interfaces.IConfigService import IConfigService
from pydo.services.TaskLoaderService import TaskLoaderService
from pydo.services.TaskRunnerService import TaskRunnerService


class TaskTests(unittest.TestCase):
    config_path: Path = Path("tests/settings/settings.json")
    config_service: IConfigService
    task_config: TaskConfig
    logger_config: LoggerConfig

    @classmethod
    def setUp(cls):
        config: IConfigService = ConfigService(cls.config_path)
        cls.config_service = config
        cls.task_config = config.get_config(TaskConfig.__name__)  # type: ignore

    def test_task_runner(self):
        task_runner = TaskRunnerService(self.config_service)
        self.assertIsNotNone(task_runner)
        task_loader = TaskLoaderService(self.config_service)
        tasks = task_loader.load_tasks()
        task_runner.run_all(tasks)


if __name__ == '__main__':
    unittest.main()
