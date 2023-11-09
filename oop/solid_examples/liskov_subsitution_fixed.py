from abc import abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, height):
        self._length = length
        self._height = height

    @property
    def area(self):
        return self._length * self._height

    def resize(self, new_length, new_height):
        self._length = new_length
        self._height = new_height


class Square(Rectangle):
    def __init__(self, side_size):
        super().__init__(side_size, side_size)

    def resize(self, new_length, new_height=None):
        # Preserve the square nature by setting both length and height to the new size
        super().resize(new_length, new_length)
