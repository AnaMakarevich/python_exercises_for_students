class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name, ": I am being constructed")

    def __del__(self):
        print(self.name, ": I am being destroyed")

    def __len__(self):
        print(self.name, ": I am being called with len()")
        return self.age


p1 = Person("Sheldon", 23)  # object creation
len(p1)
del p1
