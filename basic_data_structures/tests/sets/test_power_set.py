from basic_data_structures.class_exercises.sets.power_set import power_set


class TestCountUniqueCharacters:
    def test_1(self):
        source_set = {1, 2, 3}
        expected_result = {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}
        assert power_set(source_set) == expected_result