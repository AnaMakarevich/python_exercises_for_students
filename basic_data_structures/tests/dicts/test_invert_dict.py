from basic_data_structures.class_exercises.dicts.invert_dict import invert_dictionary

class TestCountUniqueCharacters:
    def test_1(self):
        input_dict = {'a': 1, 'b': 2, 'c': 1}
        expected_dict = {1: ['a', 'c'], 2: ['b']}
        assert invert_dictionary(input_dict) == expected_dict