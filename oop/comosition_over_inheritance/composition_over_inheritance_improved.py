from abc import abstractmethod


class Renderer:
    def render_shape(self, shape):
        pass


class ColorRenderer(Renderer):
    def render_shape(self, shape):
        print(f"Rendering {shape.__class__.__name__} with color")


class ShadowRenderer(Renderer):
    def render_shape(self, shape):
        print(f"Rendering {shape.__class__.__name__} with a shadow effect")


class GradientRenderer(Renderer):
    def render_shape(self, shape):
        print(f"Rendering {shape.__class__.__name__} with a gradient effect")


class Shape:
    def __init__(self, name, renderer):
        self.name = name
        self.renderer = renderer

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f'{self.name} with perimeter: {self.perimeter()}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

    def render(self):
        self.renderer.render_shape(self)


class Square(Shape):
    def __init__(self, name, side, renderer):
        super().__init__(name, renderer)
        self.side = side

    def perimeter(self):
        return self.side * 4


class Rectangle(Shape):
    def __init__(self, name, width, height, renderer):
        super().__init__(name, renderer)
        self.width = width
        self.height = height

    def perimeter(self):
        return (self.width + self.height) * 2


class Triangle(Shape):
    def __init__(self, name, side1, side2, side3, renderer):
        super().__init__(name, renderer)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


# Create instances of new Renderer classes
color_renderer = ColorRenderer()
shadow_renderer = ShadowRenderer()
gradient_renderer = GradientRenderer()

# Create instances of shapes with specific renderers
shapes = [Square('square', 5, color_renderer),
          Rectangle('rectangle', 2, 3, shadow_renderer),
          Triangle('triangle', 3, 4, 5, gradient_renderer),
          Square('shadowed square', 4, shadow_renderer)]

# Render all shapes
if __name__ == '__main__':
    for sh in shapes:
        print(sh)
        print(repr(sh))
        sh.render()
        print('\n')
