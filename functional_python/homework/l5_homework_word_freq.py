from functools import reduce

from utils import test_my_solution


def count_word_frequency(word_list):
    # Використовуйте reduce, щоб створити словник із частотами слів
    word_freq_dict = {}  # Замініть dummy своєю реалізацією

    return word_freq_dict


words = ["apple", "banana", "kiwi", "orange", "banana", "kiwi", "apple", "kiwi"]
expected_result = {'apple': 2, 'banana': 2, 'kiwi': 3, 'orange': 1}
actual_result = count_word_frequency(words)

test_my_solution(actual_result, expected_result)
