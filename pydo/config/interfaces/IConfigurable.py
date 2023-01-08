from abc import ABCMeta

from pydo.config.Config import Config


class IConfigurable(metaclass=ABCMeta):
    instance_name: str
    config: Config

    def __init__(self, config: Config, instance_name: str = None):
        self.config = config
        self.instance_name = instance_name if instance_name else self.__class__.__name__
