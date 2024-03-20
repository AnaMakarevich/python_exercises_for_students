from basic_data_structures.class_exercises.sets.set_operations import set_operations


class TestCountUniqueCharacters:
    def test_1(self):
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        expected = {'union': {1, 2, 3, 4, 5}, 'intersection': {3},
                    'difference': {1, 2}, 'symmetric_difference': {1, 2, 4, 5}}
        assert set_operations(set1, set2) == expected