from pydo.config.Config import Config


class LoggerConfig(Config):
    filename: str
    log_dir: str
    level: str
    logs_to_keep: int

    def __init__(self, config: dict):
        super().__init__(config)
        self.filename = self.get_property("filename")
        self.log_dir = self.get_property("log_dir")
        self.level = self.get_property("level")
        self.logs_to_keep = self.get_property("logs_to_keep")
