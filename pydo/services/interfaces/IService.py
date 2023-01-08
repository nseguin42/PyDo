from abc import ABCMeta

from pydo.services.interfaces.WithLogging import WithLogging


class IService(WithLogging, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
