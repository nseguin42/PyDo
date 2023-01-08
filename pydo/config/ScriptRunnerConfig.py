from pydo.config.ModuleConfig import ModuleConfig
from pydo.models.Script import Script


class ScriptRunnerConfig(ModuleConfig):
    script: Script

    def __init__(self, config: dict):
        super().__init__(config)

        self.script = Script(self.config["script"], self.config["lang"])
        self.is_interactive = self.config["interactive"] if "interactive" in self.config else False
