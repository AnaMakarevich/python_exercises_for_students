from abc import abstractmethod, ABC


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f'{self.name} with perimeter: {self.perimeter()}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

    @abstractmethod
    def render(self):
        pass


class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def perimeter(self):
        return self.side * 4

    def render(self):
        print(f"Rendering square with color")


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def perimeter(self):
        return (self.width + self.height) * 2

    def render(self):
        print(f"Rendering rectangle with a shadow effect")


class Triangle(Shape):
    def __init__(self, name, side1, side2, side3):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def render(self):
        print(f"Rendering triangle with a gradient effect")


class ShadowedSquare(Square):
    def __init__(self, name, side):
        super().__init__(name, side)

    def render(self):
        print(f"Rendering square with a shadow effect")


shapes = [Square('square', 5),
          Rectangle('rectangle', 2, 3),
          Triangle('triangle', 3, 4, 5),
          ShadowedSquare('shadowed square', 4)]

if __name__ == '__main__':
    for shape in shapes:
        print(shape)
        print(repr(shape))
        shape.render()
        print('\n')
