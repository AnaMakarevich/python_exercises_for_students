class Bird:
    def fly(self):
        pass


class Nightingale(Bird):
    def fly(self):
        print("Nightingale flying")


class Penguin(Bird):
    # Penguin is a bird that cannot fly
    def fly(self):
        raise NotImplementedError("Penguin cannot fly")


nightingale = Nightingale()
penguin = Penguin()

birds = [nightingale, penguin]

# This code will throw an error
for birds in birds:
    birds.fly()
