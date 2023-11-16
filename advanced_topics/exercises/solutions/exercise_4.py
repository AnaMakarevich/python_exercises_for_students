"""
Objective:
Create a custom string container class that implements the following magic methods: __str__, __len__, and __eq__.

Instructions:

    Define a class named StringContainer.
    Implement the __init__ method to initialize an empty list to store strings.
    Implement the __str__ method to return a string representation of the container.
        It should concatenate all the strings in the container, separated by spaces.
    Implement the __len__ method to return the number of strings in the container.
    Implement the __eq__ method to compare two StringContainer instances. Two instances are considered equal if they
        contain the same strings in the same order.

Мета:
Створіть спеціальний клас-контейнер строк, який реалізує наступні магічні методи: __str__, __len__ і __eq__.

Інструкції:

     Визначте клас під назвою StringContainer.
     Реалізуйте метод __init__, щоб ініціалізувати порожній список для зберігання строк.
     Реалізуйте метод __str__, щоб повернути рядкове представлення контейнера.
         Він має об’єднувати всі строки в контейнері, розділені пробілами.
     Реалізуйте метод __len__, щоб повернути кількість строк у контейнері.
     Застосуйте метод __eq__, щоб порівняти два екземпляри StringContainer. Два екземпляри вважаються рівними, якщо вони
         містять однакові строки в тому самому порядку.
    Реалізуйте метод add_string, який додає cтрок до контейнера
"""


class StringContainer:
    def __init__(self):
        self.container = []

    def __str__(self):
        return " ".join(self.container)

    def __len__(self):
        return len(self.container)

    def __eq__(self, other):
        return self.container == other.container

    def add_string(self, string):
        self.container.append(string)
