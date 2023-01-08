from pydo.config.Config import Config


class ModuleConfig(Config):

    def __init__(self, config: dict):
        super().__init__(config)

    def get_dependencies(self):
        try:
            dependsOn = self.config["dependsOn"]
            yield from dependsOn
        except KeyError:
            return []
