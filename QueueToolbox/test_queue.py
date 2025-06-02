import unittest
from queue_class import Queue  

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.q = Queue()

    def test_enqueue_single(self):
        self.q.enqueue("a")
        self.assertEqual(self.q.peek(), "a")
        self.assertEqual(self.q.size(), 1)

    def test_enqueue_multiple(self):
        items = ["a", "b", "c"]
        for item in items:
            self.q.enqueue(item)
        self.assertEqual(self.q.size(), 3)
        self.assertEqual(self.q.peek(), "a")

    def test_dequeue(self):
        self.q.enqueue("x")
        removed = self.q.dequeue()
        self.assertEqual(removed, "x")
        self.assertTrue(self.q.is_empty())

    def test_dequeue_empty(self):
        self.assertIsNone(self.q.dequeue())

    def test_peek_empty(self):
        self.assertIsNone(self.q.peek())

    def test_is_empty_true(self):
        self.assertTrue(self.q.is_empty())

    def test_is_empty_false(self):
        self.q.enqueue(10)
        self.assertFalse(self.q.is_empty())

    def test_size(self):
        self.assertEqual(self.q.size(), 0)
        self.q.enqueue("item1")
        self.assertEqual(self.q.size(), 1)
        self.q.enqueue("item2")
        self.assertEqual(self.q.size(), 2)

    def test_clear(self):
        self.q.enqueue("test")
        self.q.enqueue("clear")
        self.q.clear()
        self.assertTrue(self.q.is_empty())
        self.assertEqual(self.q.size(), 0)

    def test_contains_true(self):
        self.q.enqueue("apple")
        self.q.enqueue("banana")
        self.assertTrue(self.q.contains("banana"))

    def test_contains_false(self):
        self.q.enqueue("dog")
        self.q.enqueue("cat")
        self.assertFalse(self.q.contains("bird"))

    def test_order_preservation(self):
        self.q.enqueue("first")
        self.q.enqueue("second")
        self.q.enqueue("third")
        self.assertEqual(self.q.dequeue(), "first")
        self.assertEqual(self.q.dequeue(), "second")
        self.assertEqual(self.q.dequeue(), "third")
        self.assertTrue(self.q.is_empty())

if __name__ == "__main__":
    unittest.main()