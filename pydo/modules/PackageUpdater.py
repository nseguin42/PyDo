from pydo.config.PackageUpdaterConfig import PackageUpdaterConfig
from modules.Module import Module
from pydo.modules.ScriptRunner import ScriptRunner
from utilities.WithLogging import WithLogging


class PackageUpdater(ScriptRunner, Module, WithLogging):
    config: PackageUpdaterConfig

    def __init__(self,
                 instance_name: str, config: PackageUpdaterConfig):
        super().__init__(instance_name, config)

    def run(self):
        current_version = self.get_current_version()
        latest_version = self.get_latest_version()
        if current_version < latest_version:
            self.logger().info(f"Updating from version {current_version} to {latest_version}")
            self.run_script(self.script)

    def get_current_version(self):
        script = self.config.get_current_version_script
        return self.run_script(script)

    def get_latest_version(self):
        script = self.config.get_latest_version_script
        return self.run_script(script)
