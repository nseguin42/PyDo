from pydo.config.Config import Config


class TaskConfig(Config):
    aliases: set[str]

    def __init__(self, config: dict):
        super().__init__(config)
        if "aliases" in config:
            self.aliases = set(config["aliases"])
        else:
            self.aliases = set()

    def get_dependencies(self):
        try:
            depends_on = self.config["depends_on"]
            yield from depends_on
        except KeyError:
            return []
