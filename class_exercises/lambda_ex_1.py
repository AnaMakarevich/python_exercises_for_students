from class_exercises.utils import test_my_solution


def apply_to_each_element(numbers: list, f: callable) -> list:
    if f == "TODO":
        return None
    else:
        result = []
        for element in numbers:
            result.append(f(element))
        return result

    # Завдання: замініть TODO лямбда-функцією


source_array = [1, 2, 3, 4, 5]
expected_result = [6, 7, 8, 9, 10]
actual_result = apply_to_each_element([1, 2, 3, 4, 5], "TODO")  # Замініть dummy своєю реалізацією
test_my_solution(actual_result, expected_result)
