import unittest
from circular_queue import CircularQueue

class TestCircularQueue(unittest.TestCase):

    def setUp(self):
        self.q = CircularQueue(3)  # Small capacity for testing

    def test_initial_state(self):
        self.assertTrue(self.q.is_empty())
        self.assertFalse(self.q.is_full())
        self.assertEqual(self.q.size(), 0)

    def test_enqueue_dequeue(self):
        self.q.enqueue("a")
        self.q.enqueue("b")
        self.q.enqueue("c")
        self.assertTrue(self.q.is_full())
        self.assertEqual(self.q.dequeue(), "a")
        self.assertEqual(self.q.dequeue(), "b")
        self.assertEqual(self.q.dequeue(), "c")
        self.assertIsNone(self.q.dequeue())  # Underflow
        self.assertTrue(self.q.is_empty())

    def test_peek(self):
        self.q.enqueue("x")
        self.assertEqual(self.q.peek(), "x")
        self.q.enqueue("y")
        self.assertEqual(self.q.peek(), "x")  # Front should still be "x"
        self.q.dequeue()
        self.assertEqual(self.q.peek(), "y")

    def test_is_full_and_is_empty(self):
        self.assertTrue(self.q.is_empty())
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.assertTrue(self.q.is_full())
        self.assertFalse(self.q.is_empty())

    def test_wrap_around_behavior(self):
        self.q.enqueue("a")
        self.q.enqueue("b")
        self.q.enqueue("c")
        self.q.dequeue()  # remove "a"
        self.q.enqueue("d")  # should go to position 0
        self.assertEqual(self.q.dequeue(), "b")
        self.assertEqual(self.q.dequeue(), "c")
        self.assertEqual(self.q.dequeue(), "d")
        self.assertIsNone(self.q.dequeue())

    def test_size_tracking(self):
        self.assertEqual(self.q.size(), 0)
        self.q.enqueue(10)
        self.assertEqual(self.q.size(), 1)
        self.q.enqueue(20)
        self.q.enqueue(30)
        self.assertEqual(self.q.size(), 3)
        self.q.dequeue()
        self.assertEqual(self.q.size(), 2)

    def test_clear(self):
        self.q.enqueue("x")
        self.q.enqueue("y")
        self.q.clear()
        self.assertTrue(self.q.is_empty())
        self.assertFalse(self.q.is_full())
        self.assertIsNone(self.q.peek())
        self.assertEqual(self.q.size(), 0)
        self.assertIsNone(self.q.dequeue())

if __name__ == "__main__":
    unittest.main()
