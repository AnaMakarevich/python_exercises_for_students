# example of mixin class

class A:
    def __init__(self):
        print('A.__init__')
        super().__init__()


class B:
    def __init__(self):
        print('B.__init__')
        super().__init__()


class C1(A, B):
    def __init__(self):
        print(f'C1.__init__')
        super().__init__()


class C2(B, A):
    def __init__(self):
        print(f'C2.__init__')
        super().__init__()


if __name__ == '__main__':
    A()
    print(A.__mro__)
    print('\n')
    B()
    print(B.__mro__)
    print('\n')
    C1()
    print(C1.__mro__)
    print('\n')
    C2()
    print('\n')
    print(C2.__mro__)