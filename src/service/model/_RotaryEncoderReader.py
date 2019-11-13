from abc import ABCMeta, abstractmethod


class RotaryEncoderReader(metaclass=ABCMeta):

    @abstractmethod
    def pulse(self, callback):
        raise NotImplementedError()

    @abstractmethod
    def cancel(self, callback):
        raise NotImplementedError()
