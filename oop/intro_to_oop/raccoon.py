class Raccoon:
    animal_type = "mammal"  # переменная класса

    def __init__(self, colour_of_fur: str, size_kg: int, tail_is_present: bool = True, mood: str = "good"):
        self.current_colour_of_fur = colour_of_fur  # переменная инстанса (объекта)
        self.size = size_kg
        self.tail_is_present = tail_is_present
        self.permanent_colour_of_fur = colour_of_fur
        self._mood = mood
        self.__some_inner_state = "Raccoon's soul"

    def make_a_sound(self) -> None:
        if self._mood == "good":
            print("Grrrrrr")
        else:
            print("I will bite you")

    def wash(self) -> None:
        print(f"The raccoon is washing himself")
        self.current_colour_of_fur = self.permanent_colour_of_fur
        print(f"The fur is now {self.current_colour_of_fur}")

    def get_dirty(self) -> None:
        self.current_colour_of_fur = "black"
        print(f"The raccoon is now dirty and his fur is {self.current_colour_of_fur}")


colours = ["green", "violet", "red"]
sizes = [42, 66, 53]
moods = ["good", "bad", "good"]
raccoons = []

for c, s, m in zip(colours, sizes, moods):
    raccoons.append(Raccoon(c, s, mood=m))

for raccoon in raccoons:
    raccoon.make_a_sound()
    raccoon.get_dirty()
    raccoon.wash()
    # this will work, but it's not recommended
    r_mood = raccoon._mood
    print("\n")
    # this will raise an error because it's a private variable
    # st = raccoon.__some_inner_state
