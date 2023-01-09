from pathlib import Path

from pydo.config.Config import Config
from pydo.modules.Module import Module
from pydo.services.interfaces.IConfigService import IConfigService
from pydo.services.interfaces.IConfigurableService import IConfigurableService


class ModuleLoaderService(IConfigurableService):
    modules: list[Module] = []

    def __init__(self, config_service: IConfigService):
        super().__init__(config_service)

    def load_modules(self) -> list[Module]:
        module_dir = Path(self.config_service.get_modules_dir())
        for module_path in module_dir.iterdir():
            if not module_path.is_file():
                continue
            module = self.load_module_from_config(module_path)
            self.modules.append(module)

        self.register_dependencies()
        return self.modules

    def load_module_from_config(self, config_file_path: Path) -> Module:
        module_config = Config.load(config_file_path)
        return Module.load(module_config)

    def register_dependencies(self):
        for module in self.modules:
            module.dependencies = {modules for modules in self.modules if
                                   modules.name in module.config.get_dependencies()}
