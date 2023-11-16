import pytest

from advanced_topics.exercises.exercises.exercise_1 import calculate
from advanced_topics.exercises.tests.utils import skip_if_not_implemented


class TestCalculate:
    @skip_if_not_implemented
    def test_sum_and_product_of_integers(self):
        result = calculate(1, 2, 3, 4)
        assert result == (10, 24)

    @skip_if_not_implemented
    def test_sum_and_product_of_floats(self):
        result = calculate(0.5, 1.5, 2.5)
        assert result == (4.5, 1.875)

    @skip_if_not_implemented
    def test_sum_and_product_of_a_mix_of_integers_and_floats(self):
        result = calculate(2, 2.5, 3, 4.5)
        assert result == (12.0, 67.5)

    @skip_if_not_implemented
    def test_sum_and_product_of_negative_numbers(self):
        result = calculate(-1, -2, -3, -4)
        assert result == (-10, 24)

    @skip_if_not_implemented
    def test_sum_and_product_of_an_empty_input(self):
        result = calculate()
        assert result == (0, 1)
