from abc import ABCMeta

from pydo.config.Config import Config


class IConfigurable(metaclass=ABCMeta):
    config: Config

    def __init__(self, config: Config):
        self.config = config
