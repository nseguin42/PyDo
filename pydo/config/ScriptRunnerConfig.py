from pydo.config.TaskConfig import TaskConfig
from pydo.models.Script import Script


class ScriptRunnerConfig(TaskConfig):
    script: Script

    def __init__(self, config: dict):
        super().__init__(config)

        self.script = Script(self.config["script"])
