from device_checker import DeviceChecker


class Smartphone:
    def __init__(self, brand: str, model: str, price: float, screen_size: float):
        self.brand = brand
        self.model = model
        self.price = price
        self.screen_size = screen_size

    def display_info(self):
        print(f"{self.brand} {self.model} - ${self.price}")

    def share_internet(self):
        print(f"Sharing internet from {self.__class__.__name__}")

    def make_call(self):
        print(f"Calling from {self.brand} {self.model}")


class Laptop:
    def __init__(self, brand: str, model: str, price: float, processor: str):
        self.brand = brand
        self.model = model
        self.price = price
        self.processor = processor

    def display_info(self):
        print(f"{self.brand} {self.model} - ${self.price}")

    def share_internet(self):
        print(f"Sharing internet from {self.__class__.__name__}")

    def run_program(self):
        print(f"Running a program on {self.brand} {self.model}")


class Smartwatch:
    def __init__(self, brand: str, model: str, price: float, features: list[str]):
        self.brand = brand
        self.model = model
        self.price = price
        self.features = features

    def display_info(self):
        print(f"{self.brand} {self.model} - ${self.price}")

    def track_activity(self):
        print(f"Tracking activity with {self.brand} {self.model}")


if __name__ == "__main__":
    iphone = Smartphone("Apple", "iPhone 13", 999, 6.1)
    macbook = Laptop("Apple", "MacBook Pro", 1499, "Intel i5")
    fitbit = Smartwatch("Fitbit", "Versa 3", 229, ["Heart rate monitor", "Sleep tracking"])

    checker = DeviceChecker(smartphones=[iphone], laptops=[macbook], smartwatches=[fitbit])
    checker.check_all_devices()
