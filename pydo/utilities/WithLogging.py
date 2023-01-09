import logging
from abc import ABCMeta
from datetime import datetime
from pathlib import Path

from pydo.config.Colors import Colors
from pydo.config.LoggerConfig import LoggerConfig

log_date_format: str = "%Y-%m-%d %H:%M:%S"


def empty_file(path: Path):
    with open(path, "w") as file:
        file.write("")


def create_file(path: Path):
    for parent in path.parents:
        if not parent.exists():
            parent.mkdir()
    path.touch()


def initialize_file(path: Path):
    if path.exists():
        empty_file(path)
    else:
        create_file(path)


class WithLogging(metaclass=ABCMeta):
    """Interface for classes that have logging functionality."""

    _logger: logging.Logger
    _logger_config: LoggerConfig
    _initialized: bool

    def logger(self) -> logging.Logger:
        if not WithLogging._initialized:
            raise RuntimeError("Logger not initialized")
        return logging.getLogger(self.__class__.__name__)

    @staticmethod
    def initialize_logger(config: LoggerConfig):
        WithLogging._logger_config = config
        WithLogging._initialized = True
        formatted_filename = config.filename.format(date=datetime.now().strftime(
            log_date_format))

        path = Path(f"{config.log_dir}/{formatted_filename}")
        initialize_file(path)

        logging.basicConfig(filename=path, level=config.level)
        logging.getLogger().addHandler(logging.StreamHandler())
        logging.getLogger('asyncio').setLevel(logging.WARNING)

    @classmethod
    def cleanup_logs(cls):
        cls._logger.info("Cleaning up logs")
        path = Path(cls._logger_config.log_dir)
        files = path.glob("*.log")
        files = sorted(files, key=lambda f: f.stat().st_mtime, reverse=True)
        for file in files[cls._logger_config.logs_to_keep:]:
            cls._logger.info(f"Removing log file: {file}")
            file.unlink()

    def info(self, message: str, color: Colors = Colors.OKBLUE):
        logger = self.logger()
        logger.info(f"{color}{message.rstrip()}{Colors.ENDC}")

    def warn(self, message: str):
        logger = self.logger()
        logger.warning(f"{Colors.WARNING}{message.rstrip()}{Colors.ENDC}")

    def error(self, message: str):
        logger = self.logger()
        logger.error(f"{Colors.FAIL}{message.rstrip()}{Colors.ENDC}")
