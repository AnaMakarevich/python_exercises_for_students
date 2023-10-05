from utils import test_my_solution

source_array = [1, 2, 3, 4, 5]
expected_result = [1, 3, 5]

# TODO: відфільтрувати список так, щоб він містив лише непарні числа
actual_result = list(filter(lambda x: x % 2 != 0, source_array))

test_my_solution(actual_result, expected_result)
