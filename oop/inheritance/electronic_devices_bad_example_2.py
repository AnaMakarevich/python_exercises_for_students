import types

from device_checker import DeviceChecker


class ElectronicDevice:
    def __init__(self, brand: str, model: str, price: float):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"{self.brand} {self.model} - ${self.price}")


def make_call(self):
    print(f"Calling from {self.brand} {self.model}")


def share_internet(self):
    print(f"Sharing internet from {self.__class__.__name__}")


iphone13 = ElectronicDevice("Apple", "iPhone 13", 999)
iphone13.screen_size = 6.1
iphone13.make_call = types.MethodType(make_call, iphone13)
iphone13.share_internet = types.MethodType(share_internet, iphone13)

iphone12 = ElectronicDevice("Apple", "iPhone 12", 599)
iphone12.screen_size = 6.1
iphone12.make_call = types.MethodType(make_call, iphone12)
iphone12.share_internet = types.MethodType(share_internet, iphone12)


def run_program(self):
    print(f"Running a program on {self.brand} {self.model}")


macbook = ElectronicDevice("Apple", "MacBook Pro", 1499)
macbook.processor = "Intel i5"
macbook.run_program = types.MethodType(run_program, macbook)
macbook.share_internet = types.MethodType(share_internet, macbook)


def track_activity(self):
    print(f"Tracking activity with {self.brand} {self.model}")


fitbit = ElectronicDevice("Fitbit", "Versa 3", 229)
fitbit.features = ["Heart rate monitor", "Sleep tracking"]
fitbit.track_activity = types.MethodType(track_activity, fitbit)

if __name__ == "__main__":
    checker = DeviceChecker(smartphones=[iphone12, iphone13], laptops=[macbook], smartwatches=[fitbit])
    checker.check_all_devices()
