from pydo.config.ModuleConfig import ModuleConfig
from pydo.models.Script import Script


class ScriptRunnerConfig(ModuleConfig):
    script: Script

    def __init__(self, config: dict):
        super().__init__(config)

        self.script = Script(self.config["script"])
