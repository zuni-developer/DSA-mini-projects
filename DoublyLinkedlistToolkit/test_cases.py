import unittest
from DoublyLinkedlist import DoublyLinkedList 

class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        # Create a fresh linked list before each test
        self.dll = DoublyLinkedList()

    # ---------- INSERTION TESTS ----------
    def test_insert_at_beginning(self):
        self.dll.insert_at_beginning(10)
        self.assertEqual(self.dll.get_first(), 10)
        self.dll.insert_at_beginning(5)
        self.assertEqual(self.dll.display_forward(), [5, 10])

    def test_insert_at_end(self):
        self.dll.insert_at_end(10)
        self.assertEqual(self.dll.get_last(), 10)
        self.dll.insert_at_end(20)
        self.assertEqual(self.dll.display_forward(), [10, 20])

    def test_insert_after_node(self):
        self.dll.from_list([10, 20, 30])
        self.dll.insert_after_node(20, 25)
        self.assertEqual(self.dll.display_forward(), [10, 20, 25, 30])

    def test_insert_before_node(self):
        self.dll.from_list([10, 20, 30])
        self.dll.insert_before_node(20, 15)
        self.assertEqual(self.dll.display_forward(), [10, 15, 20, 30])

    # ---------- DELETION TESTS ----------
    def test_delete_at_beginning(self):
        self.dll.delete_at_beginning()
        self.assertTrue(self.dll.is_empty())
        self.dll.insert_at_end(10)
        self.dll.delete_at_beginning()
        self.assertTrue(self.dll.is_empty())
        self.dll.from_list([10, 20, 30])
        self.dll.delete_at_beginning()
        self.assertEqual(self.dll.display_forward(), [20, 30])

    def test_delete_at_end(self):
        self.dll.delete_at_end()
        self.assertTrue(self.dll.is_empty())
        self.dll.insert_at_end(10)
        self.dll.delete_at_end()
        self.assertTrue(self.dll.is_empty())
        self.dll.from_list([10, 20, 30])
        self.dll.delete_at_end()
        self.assertEqual(self.dll.display_forward(), [10, 20])

    def test_delete_node(self):
        self.dll.from_list([10, 20, 30])
        self.dll.delete_node(20)
        self.assertEqual(self.dll.display_forward(), [10, 30])
        self.dll.delete_node(999)  # Non-existent element
        self.assertEqual(self.dll.display_forward(), [10, 30])

    def test_delete_at_position(self):
        self.dll.from_list([10, 20, 30, 40])
        self.dll.delete_at_position(2)
        self.assertEqual(self.dll.display_forward(), [10, 20, 40])
        self.dll.delete_at_position(10)  # Out of range
        self.assertEqual(self.dll.display_forward(), [10, 20, 40])

    # ---------- SEARCH & UPDATE TESTS ----------
    def test_search(self):
        self.dll.from_list([10, 20, 30])
        self.assertTrue(self.dll.search(20))
        self.assertFalse(self.dll.search(99))

    def test_update_node(self):
        self.dll.from_list([10, 20, 30])
        self.dll.update_node(20, 25)
        self.assertEqual(self.dll.display_forward(), [10, 25, 30])
        self.dll.update_node(99, 50)  # Non-existent
        self.assertEqual(self.dll.display_forward(), [10, 25, 30])

    # ---------- DISPLAY TESTS ----------
    def test_display_forward_and_backward(self):
        self.dll.from_list([10, 20, 30])
        self.assertEqual(self.dll.display_forward(), [10, 20, 30])
        self.assertEqual(self.dll.display_backward(), [30, 20, 10])

    # ---------- UTILITY TESTS ----------
    def test_get_length_and_is_empty(self):
        self.assertTrue(self.dll.is_empty())
        self.dll.insert_at_end(10)
        self.assertFalse(self.dll.is_empty())
        self.assertEqual(self.dll.get_length(), 1)

    def test_clear(self):
        self.dll.from_list([10, 20, 30])
        self.dll.clear()
        self.assertTrue(self.dll.is_empty())

    def test_reverse(self):
        self.dll.from_list([10, 20, 30])
        self.dll.reverse()
        self.assertEqual(self.dll.display_forward(), [30, 20, 10])

    def test_get_first_and_last(self):
        self.dll.from_list([10, 20, 30])
        self.assertEqual(self.dll.get_first(), 10)
        self.assertEqual(self.dll.get_last(), 30)

    def test_get_at_position(self):
        self.dll.from_list([10, 20, 30])
        self.assertEqual(self.dll.get_at_position(1), 20)
        self.assertIsNone(self.dll.get_at_position(5))  # Out of range

    # ---------- SORT TESTS ----------
    def test_sort_ascending_and_descending(self):
        self.dll.from_list([30, 10, 20])
        self.dll.sort_ascending()
        self.assertEqual(self.dll.display_forward(), [10, 20, 30])
        self.dll.sort_descending()
        self.assertEqual(self.dll.display_forward(), [30, 20, 10])

    # ---------- MERGE & DUPLICATES ----------
    def test_merge_with(self):
        list1 = DoublyLinkedList()
        list2 = DoublyLinkedList()
        list1.from_list([10, 20])
        list2.from_list([30, 40])
        list1.merge_with(list2)
        self.assertEqual(list1.display_forward(), [10, 20, 30, 40])

    def test_remove_duplicates(self):
        self.dll.from_list([10, 20, 20, 30, 10])
        self.dll.remove_duplicates()
        self.assertEqual(sorted(self.dll.display_forward()), [10, 20, 30])

    # ---------- CONVERSION TESTS ----------
    def test_to_list_and_from_list(self):
        self.dll.from_list([1, 2, 3])
        self.assertEqual(self.dll.to_list(), [1, 2, 3])
        self.dll.clear()
        self.assertTrue(self.dll.is_empty())

if __name__ == '__main__':
    unittest.main()
