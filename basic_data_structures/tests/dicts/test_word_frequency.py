from basic_data_structures.class_exercises.dicts.word_frequency import word_frequency_counter


class TestCountUniqueCharacters:
    def test_1(self):
        input_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
        expected = {'apple': 3, 'banana': 2, 'orange': 1}
        assert word_frequency_counter(input_list) == expected

    def test_2(self):
        input_list = []
        expected = {}
        assert word_frequency_counter(input_list) == expected

    def test_3(self):
        input_list = ['apple', 'banana', '']
        expected = {'apple': 1, 'banana': 1}
        assert word_frequency_counter(input_list) == expected