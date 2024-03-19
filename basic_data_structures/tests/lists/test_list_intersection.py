from basic_data_structures.class_exercises.lists.list_intersection import list_intersection

class TestMergeTwoLists:
    def test_multiple_intersection(self):
        lst1 =[1, 2, 3, 4, 5]
        lst2 = [3, 4, 5, 6, 7]
        expected = [3, 4, 5]
        actual = list_intersection(lst1, lst2)
        assert actual == expected

    def test_no_intersection(self):
        lst1 = [1, 2, 3]
        lst2 = [4, 5, 6]
        expected = []
        actual = list_intersection(lst1, lst2)
        assert actual == expected

    def test_full_intersection(self):
        lst1 = [1, 2, 3]
        lst2 = [1, 2, 3]
        expected = [1, 2, 3]
        actual = list_intersection(lst1, lst2)
        assert actual == expected

