from abc import abstractmethod, ABC


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f'{self.name} with area: {self.area()} and perimeter: {self.perimeter()}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'


class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


class Triangle(Shape):
    def __init__(self, name, side1, side2, side3):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # compute the area of the triangle using Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


def show_all_objects():
    shapes = [Square('square', 5),
              Rectangle('rectangle', 2, 3),
              Triangle('triangle', 3, 4, 5)]
    for shape in shapes:
        print(shape)
        print(repr(shape))
        print('\n')


if __name__ == '__main__':
    show_all_objects()
    # this will raise an error because we cannot instantiate an abstract class
    abstract_shape = Shape('shape')
