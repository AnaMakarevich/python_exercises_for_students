import pytest

from advanced_topics.exercises.exercises.exercise_3 import count_keywords
from advanced_topics.exercises.tests.utils import skip_if_not_implemented


@pytest.mark.skipif(condition=True, reason="Method not implemented")
class TestCountKeywords:
    @skip_if_not_implemented
    def test_basic_keyword_counting(self):
        result = count_keywords("apple banana", "orange grape apple")
        assert result == {'apple': 2, 'orange': 1, 'banana': 1, 'grape': 1}

    @skip_if_not_implemented
    def test_case_insensitive_counting(self):
        result = count_keywords("Apple banana", "ORANGE Grape apple")
        assert result == {'apple': 2, 'orange': 1, 'banana': 1, 'grape': 1}

    @skip_if_not_implemented
    def test_excluding_specific_keywords(self):
        result3 = count_keywords("apple banana orange", "grape apple", exclude=["banana", "grape"])
        assert result3 == {'apple': 2, 'orange': 1}

    @skip_if_not_implemented
    def test_empty_input_strings(self):
        result4 = count_keywords("", "", exclude=["banana", "grape"])
        assert result4 == {}

    @skip_if_not_implemented
    def test_excluding_all_keywords(self):
        result5 = count_keywords("apple banana", "orange grape apple", exclude=["apple", "banana", "orange", "grape"])
        assert result5 == {}
