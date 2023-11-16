from unittest import TestCase

import pytest

from advanced_topics.exercises.exercises.exercise_2 import calculate_average
from advanced_topics.exercises.tests.utils import skip_if_not_implemented


@pytest.mark.skipif(condition=True, reason="Method not implemented")
class TestCalculateAverage(TestCase):
    @skip_if_not_implemented
    def test_calculate_average_of_integers(self):
        result = calculate_average([1, 2, 3], [4, 5, 6], [7, 8, 9])
        assert result == [2.0, 5.0, 8.0]

    @skip_if_not_implemented
    def test_calculate_average_of_floats(self):
        result = calculate_average([0.5, 1.5, 2.5], [3.4, 4.2, 5.1])
        result = [round(num, 4) for num in result]
        assert result == [1.5, 4.2333]

    @skip_if_not_implemented
    def test_calculate_average_of_a_mix_of_integers_and_floats(self):
        result = calculate_average([1, 2.5, 3], [4.5, 5, 6.5], [7, 8.5, 9])
        result = [round(num, 4) for num in result]
        assert result == [2.1667, 5.3333, 8.1667]

    @skip_if_not_implemented
    def test_calculate_average_of_negative_numbers(self):
        result = calculate_average([-1, -2, -3], [-4, -5, -6], [-7, -8, -9])
        assert result == [-2.0, -5.0, -8.0]

    @skip_if_not_implemented
    def test_calculate_average_of_an_empty_input(self):
        result = calculate_average()
        assert result == []
