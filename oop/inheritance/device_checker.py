class DeviceChecker:
    def __init__(self, smartphones, laptops, smartwatches):
        self.smartphones = smartphones
        self.laptops = laptops
        self.smartwatches = smartwatches

    def check_smartphones(self):
        for smartphone in self.smartphones:
            print("Checking smartphone")
            smartphone.display_info()
            smartphone.make_call()
            smartphone.share_internet()

    def check_laptops(self):
        print("Checking laptops")
        for laptop in self.laptops:
            laptop.display_info()
            laptop.run_program()
            laptop.share_internet()

    def check_smartwatches(self):
        print("Checking smartwatch")
        for smartwatch in self.smartwatches:
            smartwatch.display_info()
            smartwatch.track_activity()

    def check_all_devices(self):
        self.check_smartphones()
        print("\n")
        self.check_laptops()
        print("\n")
        self.check_smartwatches()
