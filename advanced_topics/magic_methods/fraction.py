import math


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + other_fraction.num * self.den
        new_den = self.den * other_fraction.den
        common = math.gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - other_fraction.num * self.den
        new_den = self.den * other_fraction.den
        common = math.gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        common = math.gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        common = math.gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other_fraction):
        return self.num * other_fraction.den == self.den * other_fraction.num
