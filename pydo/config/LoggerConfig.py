from pydo.config.Config import Config


class LoggerConfig(Config):
    filename: str
    log_dir: str
    level: str
    logs_to_keep: int

    def __init__(self, config: dict):
        super().__init__(config)
        self.filename = self.config["filename"]
        self.log_dir = self.config["log_dir"]
        self.level = self.config["level"]
        self.logs_to_keep = self.config["logs_to_keep"]
