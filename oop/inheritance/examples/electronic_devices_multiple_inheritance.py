from device_checker import DeviceChecker


class ElectronicDevice:
    def __init__(self, brand: str, model: str, price: float):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"{self.brand} {self.model} - ${self.price}")


class ShareInternetMixin:
    def share_internet(self):
        print(f"Sharing internet from {self.__class__.__name__}")


class Smartphone(ElectronicDevice, ShareInternetMixin):
    def __init__(self, brand: str, model: str, price: float, screen_size: float):
        super().__init__(brand, model, price)
        self.screen_size = screen_size

    def make_call(self):
        print(f"Calling from {self.brand} {self.model}")


class Laptop(ElectronicDevice, ShareInternetMixin):
    def __init__(self, brand: str, model: str, price: float, processor: str):
        super().__init__(brand, model, price)
        self.processor = processor

    def run_program(self):
        print(f"Running a program on {self.brand} {self.model}")


class Smartwatch(ElectronicDevice):
    def __init__(self, brand: str, model: str, price: float, features: list[str]):
        super().__init__(brand, model, price)
        self.features = features

    def track_activity(self):
        print(f"Tracking activity with {self.brand} {self.model}")


if __name__ == "__main__":
    iphone = Smartphone("Apple", "iPhone 13", 999, 6.1)
    macbook = Laptop("Apple", "MacBook Pro", 1499, "Intel i5")
    fitbit = Smartwatch("Fitbit", "Versa 3", 229, ["Heart rate monitor", "Sleep tracking"])

    checker = DeviceChecker(smartphones=[iphone], laptops=[macbook], smartwatches=[fitbit])
    checker.check_all_devices()
