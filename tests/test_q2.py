"""Tests for Lab 1 Question 2"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q2 import set_password


class TestSetPassword(unittest.TestCase):
    
    def test_set_password_valid_first_try(self):
        with patch('builtins.input', return_value='ValidPass123!'):
            with patch('sys.stdout', new=StringIO()):
                set_password()
                # Should exit without error
    
    def test_set_password_invalid_then_valid(self):
        inputs = ['short', 'ValidPass123!']
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new=StringIO()):
                set_password()
                # Should loop twice then exit
    
    def test_set_password_multiple_invalid(self):
        inputs = ['abc', 'nodigit!', 'NoSpecial123', 'ValidPass123!']
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new=StringIO()):
                set_password()
                # Should loop 4 times then exit


if __name__ == '__main__':
    unittest.main()