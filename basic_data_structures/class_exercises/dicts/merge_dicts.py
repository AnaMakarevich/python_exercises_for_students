"""
Write a function merge_dictionaries that takes two dictionaries as input and returns a new dictionary containing
the combined key-value pairs from both input dictionaries. If there are overlapping keys,
the values should be summed together. For example:

    >>> merge_dictionaries_by_key({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    Output: {'a': 1, 'b': 5, 'c': 4}

"""
from pathlib import Path

from basic_data_structures.class_exercises.utils import test_my_solution


def merge_dictionaries_by_key(dict1: dict, dict2: dict) -> dict:
    return {}

if __name__ == '__main__':
    test_my_solution(Path(__file__))