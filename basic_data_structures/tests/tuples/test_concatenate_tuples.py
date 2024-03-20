from basic_data_structures.class_exercises.tuples.concatenate_tuples import concatenate_tuples


class TestCountUniqueCharacters:
    def test_1(self):
        tuple1 = (1, 2, 3)
        tuple2 = (4, 5, 6)
        expected_result = (1, 2, 3, 4, 5)
        assert expected_result == concatenate_tuples(tuple1, tuple2)