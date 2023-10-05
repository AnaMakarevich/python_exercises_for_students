class Raccoon:
    def __init__(self, name, level_of_fluffiness, color):
        self.name = name
        self.color = color
        self.level_of_fluffiness = level_of_fluffiness

    def make_sound(self):
        print(f"{self.name} makes chittering sounds.")

    def gather_food(self, food_item):
        print(f"{self.name} gathers {food_item} for later.")

    def gloat(self):
        print(f"{self.name} is gloating")


raccoon1 = Raccoon("Rocky", 3, "gray")
raccoon2 = Raccoon("Bandit", 2, "black and white")
print(f"{raccoon1.name} is {raccoon1.color}.")
raccoon1.make_sound()
raccoon2.gather_food("berries")
