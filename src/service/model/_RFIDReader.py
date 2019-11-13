from abc import ABCMeta, abstractmethod
from typing import Callable


class RFIDReader(metaclass=ABCMeta):

    @abstractmethod
    async def read_forever(self, callback: Callable[[str], None]):
        raise NotImplementedError()
