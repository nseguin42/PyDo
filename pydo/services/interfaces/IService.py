from abc import ABCMeta

from pydo.utilities.WithLogging import WithLogging


class IService(WithLogging, metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
