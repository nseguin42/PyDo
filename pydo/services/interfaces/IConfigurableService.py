from abc import ABCMeta

from pydo.services.interfaces.IConfigService import IConfigService
from pydo.services.interfaces.IService import IService


class IConfigurableService(IService, metaclass=ABCMeta):
    config_service: IConfigService

    def __init__(self, config_service: IConfigService):
        super().__init__()
        self.config_service = config_service
