import pytest

from advanced_topics.exercises.exercises.exercise_5 import ComplexNumber
from advanced_topics.exercises.tests.utils import skip_if_not_implemented


class TestComplexNumber:
    @skip_if_not_implemented
    def test_complex_number_attributes(self):
        num = ComplexNumber(2, 3)
        assert num.real == 2
        assert num.imag == 3

    @skip_if_not_implemented
    def test_complex_number_string_representation(self):
        num = ComplexNumber(2, 3)
        assert str(num) == "2 + 3j"

    @skip_if_not_implemented
    def test_complex_number_equality(self):
        num1 = ComplexNumber(2, 3)
        num2 = ComplexNumber(2, 3)
        assert num1 == num2

    @skip_if_not_implemented
    def test_complex_number_inequality(self):
        num1 = ComplexNumber(2, 3)
        num2 = ComplexNumber(3, 2)
        assert num1 != num2

    @skip_if_not_implemented
    def test_complex_number_addition(self):
        num1 = ComplexNumber(2, 3)
        num2 = ComplexNumber(1, 2)
        sum_result = num1 + num2
        assert str(sum_result) == "3 + 5j"

    @skip_if_not_implemented
    def test_complex_number_subtraction(self):
        num1 = ComplexNumber(4, 5)
        num2 = ComplexNumber(1, 2)
        difference_result = num1 - num2
        assert str(difference_result) == "3 + 3j"

    @skip_if_not_implemented
    def test_complex_number_multiplication(self):
        num1 = ComplexNumber(2, 3)
        num2 = ComplexNumber(1, 2)
        product_result = num1 * num2
        assert str(product_result) == "-4 + 7j"

    @skip_if_not_implemented
    def test_complex_number_division(self):
        num1 = ComplexNumber(2, 3)
        num2 = ComplexNumber(1, 2)
        quotient_result = num1 / num2
        assert str(quotient_result) == "1.6 - 0.2j"

    @skip_if_not_implemented
    def test_complex_number_division_by_zero(self):
        num1 = ComplexNumber(1, 1)
        num2 = ComplexNumber(0, 0)
        try:
            result = num1 / num2
            assert False, "Expected ZeroDivisionError, but no exception raised"
        except ZeroDivisionError:
            pass
