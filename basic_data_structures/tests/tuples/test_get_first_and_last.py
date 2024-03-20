from basic_data_structures.class_exercises.tuples.get_first_and_last import get_first_and_last


class TestCountUniqueCharacters:
    def test_1(self):
        source_tuple = (1, 2, 3, 4, 5)
        expected = (1, 5)
        assert get_first_and_last(source_tuple) == expected