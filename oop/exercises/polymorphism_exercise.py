class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError('This area method is not implemented')

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


# TODO: create a new class called Circle that inherits from Shape

# TODO: create a new class called Pentagon that inherits from Shape

# TODO: create a new class called ShapeCollection that stores shapes in a list
# Add the following attributes:
# - shapes: a list of shapes
# Add the following methods:
# - add_shape(shape): adds a shape to the collection
# - remove_shape(shape): removes a shape from the collection
# - total_perimeter(): returns the total perimeter of all shapes in the collection
# - display_shapes_info(): displays information about each shape in the collection


class ShapeCollection:
    pass