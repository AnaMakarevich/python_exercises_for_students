from utils import test_my_solution

first_names = ["Star", "Darth", "Luke"]
last_names = ["Lord", "Vader", "Skywalker"]
expected_result = ["Star Lord", "Darth Vader", "Luke Skywalker"]

actual_result = map(lambda fn, ln: f"{fn} {ln}", first_names, last_names)

test_my_solution(actual_result, expected_result)
