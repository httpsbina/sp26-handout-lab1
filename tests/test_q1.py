"""Tests for Lab 1 Question 1"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q1 import validate_password

class TestValidatePassword(unittest.TestCase):
    
    def test_validate_password_under8characters(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = validate_password("laufey")
            self.assertFalse(result)
            self.assertIn("at least 8 characters", fake_out.getvalue())
    
    def test_validate_password_noupper(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = validate_password("laufey@2026!")
            self.assertFalse(result)
            self.assertIn("uppercase letter", fake_out.getvalue())
    
    def test_validate_password_nolower(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = validate_password("LAUFEY@2026!")
            self.assertFalse(result)
            self.assertIn("lowercase letter", fake_out.getvalue())
    
    def test_validate_password_nodigit(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = validate_password("Laufey@twentysix!")
            self.assertFalse(result)
            self.assertIn("digit", fake_out.getvalue())
    
    def test_validate_password_nospecial(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = validate_password("Laufey2026")
            self.assertFalse(result)
            self.assertIn("special character", fake_out.getvalue())
    
    def test_validate_password_nothing(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = validate_password("")
            self.assertFalse(result)
            # Should print multiple error messages
            output = fake_out.getvalue()
            self.assertIn("at least 8 characters", output)
    
    def test_validate_password_correct(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = validate_password("Laufey@2026!")
            self.assertTrue(result)
            # Should print nothing for a valid password
            self.assertEqual(fake_out.getvalue(), "")


if __name__ == '__main__':
    unittest.main()