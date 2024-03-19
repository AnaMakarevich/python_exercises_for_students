from basic_data_structures.class_exercises.lists.merge_two_lists import merge_sorted_lists


class TestMergeTwoLists:
    def test_alternating_lists(self):
        lst1 = [1, 3, 5]
        lst2 = [2, 4, 6]
        expected = [1, 2, 3, 4, 5, 6]
        actual = merge_sorted_lists(lst1, lst2)
        assert actual == expected

    def test_merge_with_left_empty_list(self):
        lst1 = []
        lst2 = [2, 4, 6]
        actual = merge_sorted_lists(lst1, lst2)
        assert actual == lst2

    def test_merge_with_right_empty_list(self):
        lst1 = [1, 2, 3]
        lst2 = []
        actual = merge_sorted_lists(lst1, lst2)
        assert actual == lst1

    def test_merge_identical_lists(self):
        lst1 = [1, 3, 5]
        lst2 = [1, 3, 5]
        expected = [1, 1, 3, 3, 5, 5]
        actual = merge_sorted_lists(lst1, lst2)
        assert expected == actual
