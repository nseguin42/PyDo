import json
from pathlib import Path

from pydo.modules.Module import Module
from pydo.services.interfaces.IConfigService import IConfigService
from pydo.services.interfaces.IConfigurableService import IConfigurableService


def get_class(name: str):
    module = __import__(f"pydo.modules.{name}", fromlist=[name])
    return getattr(module, name)


class ModuleLoaderService(IConfigurableService):
    modules: list[Module] = []

    def __init__(self, config_service: IConfigService):
        super().__init__(config_service)

    def load_modules(self) -> list[Module]:
        module_dir = Path(self.config_service.get_modules_dir())
        for module_path in module_dir.iterdir():
            if not module_path.is_file():
                continue
            module = self.load_module_from_file(module_path)
            self.modules.append(module)

        self.register_dependencies()
        return self.modules

    def load_module_from_file(self, file_path: Path) -> Module:
        data = json.loads(file_path.read_text())
        module_config = self.config_service.get_module_config(data)
        module = Module.load(module_config)
        return module

    def register_dependencies(self):
        for module in self.modules:
            module.dependencies = {modules for modules in self.modules if
                                   modules.name in module.config.get_dependencies()}
