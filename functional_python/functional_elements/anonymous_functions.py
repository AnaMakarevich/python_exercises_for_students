def square(n):
    return n ** 2


def apply_function_to_numbers(list_of_numbers, func):
    return [func(n) for n in list_of_numbers]


print(apply_function_to_numbers([1, 2, 3, 4, 5], square))


# same with anonymous function:
def apply_function_to_list(list_of_numbers, func):
    return [func(n) for n in list_of_numbers]


print(apply_function_to_numbers([1, 2, 3, 4, 5], lambda x: x ** 2))

# can easily change the function we are applying:
print(apply_function_to_numbers([1, 2, 3, 4, 5], lambda x: x - 100))
print(apply_function_to_numbers([1, 2, 3, 4, 5], lambda x: x * 3.14))
