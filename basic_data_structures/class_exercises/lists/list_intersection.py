"""
Write a Python function named list_intersection(lst1, lst2). This function should take
two lists lst1 and lst2 as input and return a new list containing
elements that are common to both lists, without any duplicates.
Example:
    >>> list_intersection([1, 2, 3, 3], [2, 3, 3])
    [2, 3]

HINT: Think if you can do the same through other data structure and if you can convert one to another
BONUS: Implement the same with loops
"""
from pathlib import Path

from basic_data_structures.class_exercises.utils import test_my_solution


def list_intersection(lst1: list[int], lst2: list[int]) -> list[int]:
    return []

if __name__ == '__main__':
    test_my_solution(Path(__file__))