def check_array(numbers, f):
    return f(x % 2 == 0 for x in numbers)


nums = (2, 4, 6, 8, 10)
print(check_array(nums, all))
