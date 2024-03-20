from basic_data_structures.class_exercises.dicts.merge_dicts import merge_dictionaries_by_key


class TestCountUniqueCharacters:
    def test_1(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        assert merge_dictionaries_by_key(dict1, dict2) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    def test_2(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        assert merge_dictionaries_by_key(dict1, dict2) == {'a': 1, 'b': 5, 'c': 4}