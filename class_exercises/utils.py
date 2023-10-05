def test_my_solution(actual_result, expected_result):
    if hasattr(actual_result, '__iter__'):
        expected_type = type(expected_result)
        actual_result = expected_type(actual_result)
        expected_result = sorted(expected_result)
        actual_result = sorted(actual_result)
    assert expected_result == actual_result, f"Incorrect: {expected_result} != {actual_result}"
    print("Success!")
