class Bird:
    def fly(self):
        pass


class Nightingale(Bird):
    def fly(self):
        print("Nightingale flying")


class Penguin(Bird):
    def fly(self):
        # some meaningful implementation of the fly
        print("Penguin swimming, not flying")


nightingale = Nightingale()
penguin = Penguin()

birds = [nightingale, penguin]

# This code will not throw an error, and each bird will execute its own fly method
for bird in birds:
    bird.fly()
