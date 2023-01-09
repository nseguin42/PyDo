from modules.Module import Module
from pydo.config.ModuleConfig import ModuleConfig

EmptyConfig: ModuleConfig = ModuleConfig({})


class DoNothingModule(Module):
    def __init__(self,
                 instance_name: str):
        super().__init__(instance_name, EmptyConfig)

    def run(self):
        pass
