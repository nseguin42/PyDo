# pydo
import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from pydo.services.ConfigService import ConfigService
from pydo.services.interfaces.IConfigService import IConfigService
from pydo.services.TaskLoaderService import TaskLoaderService
from pydo.services.TaskRunnerService import TaskRunnerService


def main(args):
    print(f"args: {args}")

    config_path = Path(args.config)
    print(f"config_path: {config_path.absolute()}")

    config_service: IConfigService = ConfigService(config_path)
    task_runner = TaskRunnerService(config_service)
    task_loader = TaskLoaderService(config_service)

    tasks = task_loader.load_tasks()
    tasks_to_run = args.tasks
    if len(tasks_to_run) > 0:
        # Check if the task has an alias in the list
        tasks = [task for task in tasks if
                 task.name in tasks_to_run or any(alias in tasks_to_run for alias in task.aliases)]

    task_runner.run_all(tasks)


parser = argparse.ArgumentParser(description="PyDo")
parser.add_argument("--tasks", help="The tasks to run (default: all)", nargs="+", default=[])
parser.add_argument("--config",
                    help="Path to config file",
                    default="settings/settings.json")
args = parser.parse_args()
main(args)
