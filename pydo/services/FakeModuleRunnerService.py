from modules.Module import Module
from pydo.services.interfaces.IConfigService import IConfigService
from pydo.services.interfaces.IModuleRunnerService import IModuleRunnerService


class FakeModuleRunnerService(IModuleRunnerService):
    """A fake module runner service that does nothing.
    """

    def __init__(self, config_service: IConfigService):
        super().__init__(config_service)

    def run(self, module: Module):
        self.logger().info(f"Running module: {module.instance_name}")
