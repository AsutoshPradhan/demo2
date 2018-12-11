import unittest
from even import is_even

class PrimesTestCase(unittest.TestCase):
    """Tests for `even.py`."""

    def test_is_five_even(self):
        """Is five successfully determined to be even?"""
        self.assertTrue(is_even(7))

if __name__ == '__main__':
    unittest.main()
