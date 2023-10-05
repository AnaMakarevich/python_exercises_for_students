from functools import reduce

from utils import test_my_solution

number = 12345
expected_result = 1 + 2 + 3 + 4 + 5
sum_of_digits = reduce(lambda x, y: int(x) + int(y), str(number))

test_my_solution(sum_of_digits, expected_result)