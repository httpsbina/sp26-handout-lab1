"""Tests for Lab 1 Question 4"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q4 import most_common_letter


class TestMostCommonLetter(unittest.TestCase):
    
    def test_most_common_letter_simple(self):
        result = most_common_letter("hello")
        self.assertEqual(result, "l")
    
    def test_most_common_letter_tie(self):
        result = most_common_letter("aabbcc")
        self.assertEqual(result, "a")  # alphabetically first
    
    def test_most_common_letter_case_insensitive(self):
        result = most_common_letter("AaAaBb")
        self.assertEqual(result, "a")
    
    def test_most_common_letter_with_numbers(self):
        result = most_common_letter("hello123world")
        self.assertEqual(result, "l")
    
    def test_most_common_letter_no_letters(self):
        result = most_common_letter("12345!@#")
        self.assertIsNone(result)
    
    def test_most_common_letter_empty_string(self):
        result = most_common_letter("")
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()