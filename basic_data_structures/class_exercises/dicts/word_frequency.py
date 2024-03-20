"""
Write a function word_frequency_counter that takes a list of words as input and returns
a dictionary where keys are unique words and values are the frequencies of those words in the list. For example:

    >>> word_frequency_counter(["apple", "banana", "apple", "orange", "banana", "apple"])
    Output: {'apple': 3, 'banana': 2, 'orange': 1}

BONUS: handle the case when an element is an empty string
"""
from pathlib import Path

from basic_data_structures.class_exercises.utils import test_my_solution


def word_frequency_counter(items: list) -> dict[str, int]:
    return {}


if __name__ == '__main__':
    test_my_solution(Path(__file__))