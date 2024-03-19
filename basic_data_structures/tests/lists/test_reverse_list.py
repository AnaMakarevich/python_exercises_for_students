from basic_data_structures.class_exercises.lists.reverse_list import reverse_list


class TestReverseList:
    def test_full_reversal(self):
        lst = [1, 2, 3, 4]
        actual = reverse_list(lst)
        expected = [4, 3, 2, 1]
        assert actual == expected

    def test_single_element(self):
        lst = [1]
        actual = reverse_list(lst)
        expected = [1]
        assert actual == expected

    def test_empty_list(self):
        lst = []
        actual = reverse_list(lst)
        expected = []
        assert actual == expected