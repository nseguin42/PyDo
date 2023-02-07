from pydo.config.PackageUpdaterConfig import PackageUpdaterConfig
from pydo.tasks.ScriptRunner import ScriptRunner
from tasks.Task import Task
from utilities.WithLogging import WithLogging
import semver;

class PackageUpdater(ScriptRunner, Task, WithLogging):
    config: PackageUpdaterConfig
    get_installed_version_script = property(lambda self: self.config.get_installed_version_script)
    get_latest_version_script = property(lambda self: self.config.get_latest_version_script)

    def __init__(self, config: PackageUpdaterConfig):
        super().__init__(config)

    def run(self):
        installed_version = self.get_installed_version()
        latest_version = self.get_latest_version()
        self.info(f"Installed version: {installed_version}")
        self.info(f"Latest version: {latest_version}")
        if installed_version.compare(latest_version) < 0:
            self.logger().info(f"Updating from version {installed_version} to {latest_version}")
            self.run_script(self.script)
        else:
            self.info("No update available")

    def get_installed_version(self):
        script = self.get_installed_version_script
        return semver.VersionInfo.parse(self.run_script(script))

    def get_latest_version(self):
        script = self.get_latest_version_script
        return semver.VersionInfo.parse(self.run_script(script))

