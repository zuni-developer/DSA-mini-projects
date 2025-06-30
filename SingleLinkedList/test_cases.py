import unittest
from SingleLinkedList import SingleLinkedList

class TestSingleLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = SingleLinkedList()

    def test_insert_methods(self):
        self.ll.insert_at_beginning(10)
        self.ll.insert_at_end(20)
        self.ll.insert_at_index(1, 15)
        self.assertEqual(self.ll.to_list(), [10, 15, 20])

    def test_insert_at_index_out_of_range(self):
        self.ll.insert_at_end(1)
        self.ll.insert_at_index(100, 99)  # should not insert
        self.assertEqual(self.ll.size, 1)

    def test_delete_methods(self):
        self.ll.from_list([1, 2, 3, 4])
        self.ll.delete_at_beginning()
        self.assertEqual(self.ll.to_list(), [2, 3, 4])

        self.ll.delete_at_end()
        self.assertEqual(self.ll.to_list(), [2, 3])

        self.ll.delete_at_index(0)
        self.assertEqual(self.ll.to_list(), [3])

    def test_search_and_get_set(self):
        self.ll.from_list([5, 10, 15])
        self.assertTrue(self.ll.search(10))
        self.assertFalse(self.ll.search(100))

        self.assertEqual(self.ll.get(1), 10)
        self.ll.set(1, 12)
        self.assertEqual(self.ll.get(1), 12)

    def test_reverse(self):
        self.ll.from_list([1, 2, 3])
        self.ll.reverse()
        self.assertEqual(self.ll.to_list(), [3, 2, 1])

    def test_length_and_is_empty(self):
        self.assertTrue(self.ll.is_empty())
        self.ll.insert_at_end(42)
        self.assertFalse(self.ll.is_empty())
        self.assertEqual(self.ll.length(), 1)

    def test_get_middle(self):
        self.ll.from_list([1, 2, 3, 4, 5])
        middle = self.ll.get_middle()
        self.assertEqual(middle.data, 3)

    def test_clear(self):
        self.ll.from_list([1, 2, 3])
        self.ll.clear()
        self.assertTrue(self.ll.is_empty())

    def test_from_list_and_merge(self):
        self.ll.from_list([1, 2, 3])
        other = SingleLinkedList()
        other.from_list([100, 200])
        self.ll.merge(other)
        self.assertEqual(self.ll.to_list(), [1, 2, 3, 100, 200])

    def test_remove_by_value(self):
        self.ll.from_list([10, 20, 30])
        self.ll.remove_by_value(20)
        self.assertEqual(self.ll.to_list(), [10, 30])

    def test_find_nth_from_end(self):
        self.ll.from_list([10, 20, 30, 40, 50])
        value = self.ll.find_nth_from_end(1)
        self.assertEqual(value, 50)
        value2 = self.ll.find_nth_from_end(3)
        self.assertEqual(value2, 30)

    def test_sort(self):
        self.ll.from_list([30, 10, 20])
        self.ll.sort()
        self.assertEqual(self.ll.to_list(), [10, 20, 30])

if __name__ == '__main__':
    unittest.main()
