"""
Write a function invert_dictionary that takes a dictionary as input and returns a new dictionary where
the keys are the values from the input dictionary, and the values are lists of keys
 from the input dictionary that had the corresponding value. For example:

    >>> invert_dictionary({'a': 1, 'b': 2, 'c': 1})
    Output: {1: ['a', 'c'], 2: ['b']}

"""
from pathlib import Path

from basic_data_structures.class_exercises.utils import test_my_solution


def invert_dictionary(d: dict) -> dict:
    return {}

if __name__ == '__main__':
    test_my_solution(Path(__file__))