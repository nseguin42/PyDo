# pydo
import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from pydo.services.ConfigService import ConfigService
from pydo.services.interfaces.IConfigService import IConfigService
from pydo.services.ModuleLoaderService import ModuleLoaderService
from pydo.services.ModuleRunnerService import ModuleRunnerService


def main(args):
    print(f"args: {args}")

    config_path = Path(args.config)
    print(f"config_path: {config_path.absolute()}")

    config_service: IConfigService = ConfigService(config_path)
    module_runner = ModuleRunnerService(config_service)
    module_loader = ModuleLoaderService(config_service)

    modules = module_loader.load_modules()
    modules_to_run = args.modules
    if len(modules_to_run) > 0:
        modules = list(filter(lambda m: m.name in modules_to_run, modules))

    module_runner.run_all(modules)


parser = argparse.ArgumentParser(description="PyDo")
parser.add_argument("--modules", help="The modules to run (default: all)", nargs="+", default=[])
parser.add_argument("--config",
                    help="Path to config file",
                    default="settings/settings.json")
args = parser.parse_args()
main(args)
