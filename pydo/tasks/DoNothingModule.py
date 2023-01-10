from pydo.config.TaskConfig import TaskConfig
from tasks.Task import Task

EmptyConfig: TaskConfig = TaskConfig({})


class DoNothingTask(Task):
    def __init__(self,
                 instance_name: str):
        super().__init__(instance_name, EmptyConfig)

    def run(self):
        pass
