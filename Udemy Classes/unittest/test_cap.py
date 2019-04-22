"""Unit Testing Class"""

import unittest
import cap

class TestCap(unittest.TestCase):
    """Test Capitalization class"""

    def test_one_word(self):
        """Test single word sentence"""
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        """Test multiple words sentence"""
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty python')

if __name__ == '__main__':
    unittest.main()
