from pydo.config.ScriptRunnerConfig import ScriptRunnerConfig
from pydo.models.Script import Script


class PackageUpdaterConfig(ScriptRunnerConfig):
    script: Script = None
    get_installed_version_script: Script = None
    get_latest_version_script: Script = None

    def __init__(self, config: dict):
        super().__init__(config)

        self.get_installed_version_script = Script(self.config["get_installed_version_script"],
                                                   "sh")
        self.get_latest_version_script = Script(self.config["get_latest_version_script"], "sh")
