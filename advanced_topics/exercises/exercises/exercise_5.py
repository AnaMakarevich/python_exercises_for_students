"""
Objective:
Create a class named ComplexNumber that represents complex numbers and implement the magic methods for basic arithmetic operations.

Instructions:

    Define a class named ComplexNumber with attributes real and imag representing the real and imaginary parts of a
    complex number.
    Implement the __init__ method to initialize the real and imaginary parts.
    Implement the __str__ method to return a string representation of the complex number in the form "real + imagj".
    Implement the __add__, __sub__, __mul__, and __truediv__ methods to enable addition, subtraction, multiplication, \
    and division of complex numbers.
    Implement the __eq__ method to compare two ComplexNumber instances. Two instances are considered equal if they have
    the same real and imaginary parts.

Мета:
Створіть клас під назвою ComplexNumber, який представлятиме комплексні числа та реалізуйте магічні методи для основних
арифметичних операцій.

Інструкції:

     Визначте клас під назвою ComplexNumber з атрибутами real і imag, що представляють дійсну та уявну частини
     комплексне число.
     Реалізуйте метод __init__ для ініціалізації реальних і уявних частин.
     Застосуйте метод __str__, щоб повернути рядкове представлення комплексного числа у формі «real + imagj».
     Застосуйте методи __add__, __sub__, __mul__ і __truediv__, щоб увімкнути додавання, віднімання, множення, \
     і ділення комплексних чисел.
     Застосуйте метод __eq__, щоб порівняти два екземпляри ComplexNumber. Два екземпляри вважаються рівними,
     якщо вони мають однакові дійсну та уявну частини.
"""


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        # TODO: Implement this method
        raise NotImplementedError

    def __add__(self, other):
        # TODO: Implement this method
        raise NotImplementedError

    def __sub__(self, other):
        # TODO: Implement this method
        raise NotImplementedError

    def __mul__(self, other):
        # TODO: Implement this method
        raise NotImplementedError

    def __truediv__(self, other):
        # TODO: Implement this method
        raise NotImplementedError

    def __eq__(self, other):
        # TODO: Implement this method
        raise NotImplementedError

