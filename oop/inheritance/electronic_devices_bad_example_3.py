from device_checker import DeviceChecker


class ElectronicDevice:
    def __init__(self, brand: str, model: str, price: float):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"{self.brand} {self.model} - ${self.price}")


# modify classes and add the methods we need
def make_call(self):
    print(f"Calling from {self.brand} {self.model}")


def share_internet(self):
    print(f"Sharing internet from {self.__class__.__name__}")


smartphone_methods = {**ElectronicDevice.__dict__, 'make_call': make_call, 'share_internet': share_internet}
Smartphone = type('Smartphone', ElectronicDevice.__bases__, smartphone_methods)


def run_program(self):
    print(f"Running a program on {self.brand} {self.model}")


laptop_methods = {**ElectronicDevice.__dict__, 'run_program': run_program, 'share_internet': share_internet}
Laptop = type('Laptop', ElectronicDevice.__bases__, laptop_methods)


def track_activity(self):
    print(f"Tracking activity with {self.brand} {self.model}")


smartwatch_methods = {**ElectronicDevice.__dict__, 'track_activity': track_activity}
Smartwatch = type('Smartwatch', ElectronicDevice.__bases__, smartwatch_methods)

iphone13 = Smartphone("Apple", "iPhone 13", 999)
iphone13.screen_size = 6.1
iphone12 = Smartphone("Apple", "iPhone 12", 599)
iphone12.screen_size = 6.1

macbook = Laptop("Apple", "MacBook Pro", 1499)
macbook.processor = "Intel i5"

fitbit = Smartwatch("Fitbit", "Versa 3", 229)
fitbit.features = ["Heart rate monitor", "Sleep tracking"]

if __name__ == "__main__":
    checker = DeviceChecker(smartphones=[iphone12, iphone13], laptops=[macbook], smartwatches=[fitbit])
    checker.check_all_devices()
