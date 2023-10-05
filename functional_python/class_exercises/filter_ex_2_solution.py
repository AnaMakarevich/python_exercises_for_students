from utils import test_my_solution

source_array = ["orange", "banana", "beer", "wine", "apple", "grape"]
expected_result = ['apple', 'grape']

# TODO: скористайтеся функцією фільтра, щоб відфільтрувати слова, які мають довжину 5 (список повинен містити лише
#  слова з рівно 5 літер)
actual_result = list(filter(lambda s: len(s) == 5, source_array))

test_my_solution(actual_result, expected_result)
