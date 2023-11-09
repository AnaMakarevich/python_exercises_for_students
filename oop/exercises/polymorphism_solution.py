from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        raise NotImplementedError('This area method is not implemented')

    @abstractmethod
    def perimeter(self):
        raise NotImplementedError('This perimeter method is not implemented')

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


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        # circumference
        return 2 * 3.14 * self.radius


class Pentagon(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def area(self):
        # compute the area of the pentagon using Heron's formula
        return 1.72 * self.side ** 2

    def perimeter(self):
        return self.side * 5


class ShapeCollection:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def remove_shape(self, shape):
        self.shapes.remove(shape)

    def total_perimeter(self):
        total = 0
        for shape in self.shapes:
            total += shape.perimeter()
        return total

    def display_shapes_info(self):
        for shape in self.shapes:
            print(shape)


if __name__ == '__main__':
    # create shapes collections
    shapes = ShapeCollection()
    # add shapes
    shapes.add_shape(Square('square', 5))
    shapes.add_shape(Rectangle('rectangle', 2, 3))
    shapes.add_shape(Triangle('triangle', 3, 4, 5))
    shapes.add_shape(Circle('circle', 5))
    shapes.add_shape(Pentagon('pentagon', 5))
    # display shapes info
    print('Shapes info:')
    shapes.display_shapes_info()
    # display total perimeter
    print(f'Total perimeter: {shapes.total_perimeter()}')
    # remove a shape
    shapes.remove_shape(shapes.shapes[0])
    # display shapes info
    print('Shapes info:')
    shapes.display_shapes_info()
