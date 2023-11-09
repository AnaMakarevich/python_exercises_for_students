"""""
У вас є колекція різних фігур, включаючи Square, Rectangle and Triangle
Кожна фігура має спільні характеристики, успадковані від базового класу Shape.


1. Створіть дві нові фігури: Circle та Pentagon. Переконайтеся, що кожен клас форми є похідним від базового класу Shape.

2. Реалізуйте колекцію фігур, яка зберігає ці об’єкти. Колекція повинна мати можливість обробляти різні форми. The
клас повинен мати методи для додавання фігур до колекції та відображення інформації про кожну фігуру в колекції.

3. Створіть приклад використання для класу `ShapeCollection`. Приклад має продемонструвати, що колекція може обробляти
різні форми.
"""""


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


# TODO: створити новий клас під назвою Circle, який успадковує Shape

# TODO: створити новий клас під назвою Pentagon, який успадковує Shape

# TODO: створити новий клас під назвою ShapeCollection, який зберігає фігури у списку
# Додайте такі атрибути::
# - shapes: список форм
# Додайте такі методи:
# - add_shape(shape): додає форму до колекції
# - remove_shape(shape): видаляє форму з колекції
# - total_perimeter(): повертає загальний периметр усіх фігур у колекції
# - display_shapes_info(): відображає інформацію про кожну форму в колекції


class ShapeCollection:
    pass
