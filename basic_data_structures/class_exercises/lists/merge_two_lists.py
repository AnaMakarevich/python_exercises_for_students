"""
Write a Python function named merge_sorted_lists(lst1, lst2). This function should
take two sorted lists lst1 and lst2 as input and return a new list that contains
all elements from both lists in sorted order. Note that the lists might contain the SAME elements.
For example, 1 can be both in lst1 and lst2. Both occurrences should be in the final list.
Example:
    >>> merge_sorted_lists([1, 2, 3], [1, 4, 5])
    [1, 1, 2, 3, 4, 5]

HINT: Look for built-in methods
BONUS: Implement the same with loops
"""
from pathlib import Path

from basic_data_structures.class_exercises.utils import test_my_solution


def merge_sorted_lists(lst1: list[int], lst2: list[int]) -> list[int]:
    return []

if __name__ == '__main__':
    test_my_solution(Path(__file__))