from basic_data_structures.class_exercises.lists.count_occurrences import count_occurrences


class TestCountOccurrences:
    def test_count_occurrences(self):
        lst, element = [1, 2, 3, 4, 2, 2, 3], 3
        actual = count_occurrences(lst=lst, element=element)
        expected = 2
        assert actual == expected

    def test_count_occurrences_empty_list(self):
        lst, element = [], 0
        actual = count_occurrences(lst=lst, element=element)
        expected = 0
        assert actual == expected

    def test_when_no_occurrences_in_list(self):
        lst, element = [1, 2, 4], 42
        actual = count_occurrences(lst=lst, element=element)
        expected = 0
        assert actual == expected