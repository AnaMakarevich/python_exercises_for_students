from utils import test_my_solution

source_array = [1, 2, 3, 4, 5]
expected_result = [1, 4, 9, 16, 25]

# TODO: Використовуйте функцію map, щоб звести кожне число в список у квадрат.
actual_result = list(map(lambda x: x**2, source_array))

test_my_solution(actual_result, expected_result)