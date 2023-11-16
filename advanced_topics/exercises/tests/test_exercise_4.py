import pytest

from advanced_topics.exercises.exercises.exercise_4 import StringContainer
from advanced_topics.exercises.tests.utils import skip_if_not_implemented


@pytest.mark.skipif(condition=True, reason="Method not implemented")
class TestStringContainer:
    @skip_if_not_implemented
    def test_empty_container(self):
        container1 = StringContainer()
        assert str(container1) == ""
        assert len(container1) == 0

    @skip_if_not_implemented
    def test_add_string(self):
        container2 = StringContainer()
        container2.add_string("Hello")
        container2.add_string("world")
        assert str(container2) == "Hello world"
        assert len(container2) == 2

    @skip_if_not_implemented
    def test_equality(self):
        container3 = StringContainer()
        container3.add_string("Hello")
        container3.add_string("world")
        container4 = StringContainer()
        container4.add_string("Hello")
        container4.add_string("world")
        assert container3 == container4

    @skip_if_not_implemented
    def test_inequality(self):
        container5 = StringContainer()
        container5.add_string("Hello")
        container5.add_string("world")
        container6 = StringContainer()
        container6.add_string("Hello")
        container6.add_string("Python")
        assert container5 != container6

    @skip_if_not_implemented
    def test_complex_strings(self):
        container7 = StringContainer()
        container7.add_string("This is")
        container7.add_string("a test")
        container7.add_string("for strings")
        assert str(container7) == "This is a test for strings"
