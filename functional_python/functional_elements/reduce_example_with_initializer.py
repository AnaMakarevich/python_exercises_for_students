from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum_num = reduce(lambda x, y: x + y, numbers, 10)

print(sum_num)
