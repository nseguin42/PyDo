import unittest
from pathlib import Path

from pydo.services.ConfigService import ConfigService
from pydo.services.interfaces.IConfigService import IConfigService
from pydo.config.LoggerConfig import LoggerConfig
from pydo.config.ModuleConfig import ModuleConfig
from pydo.services.ModuleLoaderService import ModuleLoaderService
from pydo.services.ModuleRunnerService import ModuleRunnerService


class ModuleTests(unittest.TestCase):
    config_path: Path = Path("tests/settings/settings.json")
    config_service: IConfigService
    module_config: ModuleConfig
    logger_config: LoggerConfig

    @classmethod
    def setUp(cls):
        config: IConfigService = ConfigService(cls.config_path)
        cls.config_service = config
        cls.module_config = config.get_config(ModuleConfig.__name__)  # type: ignore

    def test_module_runner(self):
        module_runner = ModuleRunnerService(self.config_service)
        self.assertIsNotNone(module_runner)
        module_loader = ModuleLoaderService(self.config_service)
        modules = module_loader.load_modules()
        module_runner.run_all(modules)


if __name__ == '__main__':
    unittest.main()
