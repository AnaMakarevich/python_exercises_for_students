from basic_data_structures.class_exercises.sets.count_unique_characters import count_unique_characters


class TestCountUniqueCharacters:
    def test_1(self):
        word = 'hello'
        assert count_unique_characters(word) == 4

    def test_2(self):
        word = ''
        assert count_unique_characters(word) == 0