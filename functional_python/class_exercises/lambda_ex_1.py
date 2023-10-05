from utils import test_my_solution


def apply_to_each_element(numbers: list, f: callable) -> list | None:
    if f == "TODO":
        return None
    else:
        result = []
        for element in numbers:
            result.append(f(element))
        return result


source_array = [1, 2, 3, 4, 5]
expected_result = [6, 7, 8, 9, 10]
actual_result = apply_to_each_element(source_array, "TODO")  # Замініть dummy своєю реалізацією
test_my_solution(actual_result, expected_result)
