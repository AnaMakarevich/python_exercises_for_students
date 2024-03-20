"""
Write a function power_set that takes a set as input and returns a set containing all
possible subsets (including the empty set and the set itself). For example:

    >>> power_set({1, 2, 3})
    Output: {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}

"""
from pathlib import Path

from basic_data_structures.class_exercises.utils import test_my_solution


def power_set(source_set: set) -> set:
    return set()

if __name__ == '__main__':
    test_my_solution(Path(__file__))