class LightBulb:
    def turn_on(self):
        print("LightBulb: ON")


class Switch:
    def __init__(self, bulb):
        self.bulb = bulb

    def operate(self):
        self.bulb.turn_on()


if __name__ == '__main__':
    bulb = LightBulb()
    switch = Switch(bulb)
    switch.operate()
