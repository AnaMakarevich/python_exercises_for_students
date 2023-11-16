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
        sign = "+" if self.imag >= 0 else "-"
        print("SIGN", sign)
        return f"{self.real} {sign} {abs(self.imag)}j"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        # multiply complex numbers
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        # divide complex numbers
        denominator = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real, imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

