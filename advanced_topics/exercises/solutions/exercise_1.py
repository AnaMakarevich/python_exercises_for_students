"""Define a function calculate that takes a variable number of arguments (*args) and returns a tuple containing the
sum and product of all the arguments.

Визначте функцію обчислення, яка приймає змінну кількість аргументів (*args) і
повертає кортеж, що містить суму та добуток усіх аргументів.


BONUS TASK
Bonus task: implement the product and sum using reduce and lambda functions
Бонусне завдання: реалізувати добуток і суму за допомогою функції reduce та лямбда-функцій.
"""
from functools import reduce


def calculate(*args) -> tuple:
    sum_ = reduce(lambda x, y: x + y, args, 0)
    product = reduce(lambda x, y: x * y, args, 1)
    return sum_, product
