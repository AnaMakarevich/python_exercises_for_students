# Basic example to show method resolution

# Path: mro_example_1.py

class A:
    @staticmethod
    def method():
        print('A.method')


class B(A):
    @staticmethod
    def method():
        print('B.method')


if __name__ == '__main__':
    print("Methods output")
    print("Class A")
    A().method()
    print("A.__mro__:", A.__mro__)
    print('\n')
    print("Class B")
    B().method()
    print("B.__mro__:", B.__mro__)
