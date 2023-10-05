def check_array(numbers, f):
    return f(x % 2 == 0 for x in numbers)


numbers = (2, 4, 6, 8, 10)
print(check_array(numbers, all))
