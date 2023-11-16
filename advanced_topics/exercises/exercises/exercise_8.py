"""Objective: Implement a Python class SimpleContainer that acts as a simple container. The class should allow adding
items, retrieving items by index, and provide an iterable interface.

Instructions:

    Implement the SimpleContainer class.
    The class should have a list to store items.
    Implement a method add_item(item) to add items to the container.
    Implement a method get_item(index) to retrieve items by index.
    Implement the __len__ method to return the number of items in the container.
    Implement the __iter__ method to make the container iterable.
    Implement the __next__ method to make the container iterable.

Мета: реалізувати клас Python SimpleContainer, який діє як простий контейнер. Клас має дозволяти додавання
елементів, отримання елементів за індексом і надання ітераційного інтерфейсу.

Інструкції:

     Реалізуйте клас SimpleContainer.
     Клас має мати список для зберігання елементів.
     Реалізуйте метод add_item(item), щоб додати елементи до контейнера.
     Реалізуйте метод get_item(index), щоб отримати елементи за індексом.
     Застосуйте метод __len__, щоб повернути кількість елементів у контейнері.
     Реалізуйте метод __iter__, щоб зробити контейнер повторюваним.
     Реалізуйте метод __next__, щоб зробити контейнер ітеративним.
"""


class SimpleContainer:
    def __init__(self):
        self.items = []
        self.iter_index = 0

    def add_item(self, item):
        raise NotImplementedError

    def __getitem__(self, index):
        raise NotImplementedError

    def __setitem__(self, index, value):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __next__(self):
        raise NotImplementedError

