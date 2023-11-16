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

Мета: реалізувати клас Python SimpleContainer, який діє як простий контейнер. Клас повинен дозволяти додавання
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
        self.items.append(item)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        if self.iter_index < len(self.items):
            result = self.items[self.iter_index]
            self.iter_index += 1
            return result
        else:
            raise StopIteration

