# Function with *args and **kwargs
def print_arguments(*args, **kwargs):
    print("Length of positional arguments:", len(args))
    print("Length of keyword arguments:", len(kwargs))

    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)


# Example 1: Using *args and **kwargs
print_arguments(1, 2, 3, name='John', age=25)

# Example 2: Unpacking elements from iterables
my_list = [4, 5, 6]
my_dict = {'city': 'New York', 'country': 'USA'}
print_arguments(*my_list, **my_dict)


def some_library_function(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


# example of unpacking an iterable

list_A = [1, 2, 3]
list_B = [4, 5, 6]
list_C = [*list_A, *list_B]  # [1, 2, 3, 4, 5, 6]


def process_args(*args):
    for arg in args:
        print(arg)


process_args(*list_A)  # 1 2 3

dict_A = {'a': 1, 'b': 2}
dict_B = {'c': 3, 'd': 4}
dict_C = {**dict_A, **dict_B}  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


def process_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


process_kwargs(**dict_A)  # a 1 b 2
