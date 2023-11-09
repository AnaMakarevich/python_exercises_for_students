from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def operate(self):
        pass


class LightBulb(Switchable):
    def operate(self):
        print("LightBulb: ON")


class Switch:
    def __init__(self, device):
        self.device = device

    def operate(self):
        self.device.operate()


if __name__ == '__main__':
    bulb = LightBulb()
    switch = Switch(bulb)
    switch.operate()
