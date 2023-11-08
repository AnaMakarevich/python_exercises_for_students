class A:
    @staticmethod
    def method():
        print('A.method')


class B(A):
    @staticmethod
    def method():
        print('B.method')


class C(A):
    @staticmethod
    def method():
        print('C.method')


class D(B, C):
    pass


# the following example will produce error
# class E(C, D):
#    pass

if __name__ == '__main__':
    print("Class A")
    A().method()
    print("A.__mro__:", A.__mro__)
    print('\n')
    print("Class B")
    B().method()
    print("B.__mro__:", B.__mro__)
    print('\n')
    print("Class C")
    C().method()
    print("C.__mro__:", C.__mro__)
    print('\n')
    print("Class D")
    D().method()
    print("D.__mro__:", D.__mro__)
    print('\n')
