# Example of multilevel inheritance and method resolution order

# Path: multilevel_inheritance_mro_example.py


class Elephant:
    @staticmethod
    def make_sound():
        print("Trump trump")


class Penguin:
    @staticmethod
    def make_sound():
        print("Chirp chirp")


# classes ordering
class Pengelephant(Penguin, Elephant):
    def __init__(self):
        print("Big scary PengElephant")


class Elethenguin(Elephant, Penguin):
    def __init__(self):
        print("Small funny Elethenguin")


if __name__ == '__main__':
    print(Pengelephant.__mro__)
    print(Elethenguin.__mro__)
    pengelephant = Pengelephant()
    pengelephant.make_sound()

    elethenguin = Elethenguin()
    elethenguin.make_sound()
