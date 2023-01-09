from modules.Module import Module
from pydo.config.PackageUpdaterConfig import PackageUpdaterConfig
from pydo.modules.ScriptRunner import ScriptRunner
from utilities.WithLogging import WithLogging


class PackageUpdater(ScriptRunner, Module, WithLogging):
    config: PackageUpdaterConfig
    get_installed_version_script = property(lambda self: self.config.get_installed_version_script)
    get_latest_version_script = property(lambda self: self.config.get_latest_version_script)

    def __init__(self, config: PackageUpdaterConfig):
        super().__init__(config)

    def run(self):
        current_version = self.get_current_version()
        latest_version = self.get_latest_version()
        if current_version < latest_version:
            self.logger().info(f"Updating from version {current_version} to {latest_version}")
            self.run_script(self.script)

    def get_current_version(self):
        script = self.get_installed_version_script
        return self.run_script(script)

    def get_latest_version(self):
        script = self.get_latest_version_script
        return self.run_script(script)
