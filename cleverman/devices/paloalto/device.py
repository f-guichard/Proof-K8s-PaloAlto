from abc import ABC, abstractmethod
from dataclasses import dataclass


class Device(ABC):


    @abstractmethod
    def get_device_info(self):
        pass


@dataclass
class PaloAlto(Device):
    '''Palo Alto Firewall'''

    name: str = None
    virtual_systems: dict = None


    def make_device(self, raw_config: str) -> None:
        pass

    def get_device_info(self) -> list:
        return [self.name, self.virtual_systems]