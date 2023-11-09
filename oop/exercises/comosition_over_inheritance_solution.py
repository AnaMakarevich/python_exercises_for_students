class Engine:
    @staticmethod
    def start():
        print("Engine started")

    @staticmethod
    def stop():
        print("Engine stopped")


class ElectricEngine(Engine):
    @staticmethod
    def charge():
        print("Electric engine is charging")


class GasEngine(Engine):
    @staticmethod
    def refuel():
        print("Gas engine is refueling")


class Car:
    def __init__(self, engine):
        self.engine = engine

    @staticmethod
    def drive():
        print("Car is moving")

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()


if __name__ == '__main__':
    gas_engine = GasEngine()
    my_car = Car(gas_engine)
    my_car.start()
    my_car.drive()
    my_car.stop()

    electric_engine = ElectricEngine()
    my_electric_car = Car(electric_engine)
    my_electric_car.start()
    my_electric_car.drive()
    my_electric_car.stop()
