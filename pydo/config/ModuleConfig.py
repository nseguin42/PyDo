from pydo.config.Config import Config


class ModuleConfig(Config):
    def __init__(self, config: dict):
        super().__init__(config)

    def get_dependencies(self):
        try:
            depends_on = self.config["depends_on"]
            yield from depends_on
        except KeyError:
            return []
