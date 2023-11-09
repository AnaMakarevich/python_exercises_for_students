from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height, position):
        super().__init__(position)
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing a rectangle at position {self.position} with width {self.width} and height {self.height}.")


class ColouredRectangle(Rectangle):
    def __init__(self, width, height, position, color):
        super().__init__(width, height, position)
        self.color = color

    def draw_with_color(self):
        print(f"Drawing a {self.color} rectangle at position {self.position} with width {self.width} and height {self.height}.")


if __name__ == '__main__':
    rectangle = Rectangle(5, 3, (0, 0))
    rectangle.draw()

    coloured_rectangle = ColouredRectangle(5, 3, (2, 2), "red")
    coloured_rectangle.draw_with_color()
