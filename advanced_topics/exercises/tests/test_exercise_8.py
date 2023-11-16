import pytest

from advanced_topics.exercises.exercises.exercise_8 import SimpleContainer
from advanced_topics.exercises.tests.utils import skip_if_not_implemented


@pytest.mark.skipif(condition=True, reason="Method not implemented")
class TestSimpleContainer:
    @staticmethod
    def __get_basic_container():
        container = SimpleContainer()
        container.add_item("Apple")
        container.add_item("Banana")
        container.add_item("Orange")
        return container

    @skip_if_not_implemented
    def test_simple_container(self):
        # Create a SimpleContainer instance
        container = SimpleContainer()

        # Add items
        container.add_item("Apple")
        container.add_item("Banana")
        container.add_item("Orange")
        assert len(container) == 3, "Test 4 Failed: Incorrect length"

    @skip_if_not_implemented
    def test_simple_container_get_item(self):
        container = self.__get_basic_container()
        assert container[0] == "Apple", "Test 1 Failed: Incorrect item retrieved by index"
        assert container[2] == "Orange", "Test 2 Failed: Incorrect item retrieved by index"
        assert len(container) == 3, "Test 4 Failed: Incorrect length"

    @skip_if_not_implemented
    def test_simple_container_set_item(self):
        container = self.__get_basic_container()
        container[1] = "Grapes"
        assert container[1] == "Grapes", "Test 3 Failed: Incorrect item set by index"

    @skip_if_not_implemented
    def test_simple_container_iter(self):
        container = self.__get_basic_container()
        iterator = iter(container)
        assert next(iterator) == "Apple", "Incorrect item during iteration"
        assert next(iterator) == "Banana", "Incorrect item during iteration"
        assert next(iterator) == "Orange", "Incorrect item during iteration"

    @skip_if_not_implemented
    def test_simple_container_iter_explicit(self):
        container = self.__get_basic_container()
        iterator = iter(container)
        assert next(iterator) == "Apple", "Test 8 Failed: Incorrect item using next"
        assert next(iterator) == "Banana", "Test 9 Failed: Incorrect item using next"
        assert next(iterator) == "Orange", "Test 10 Failed: Incorrect item using next"
