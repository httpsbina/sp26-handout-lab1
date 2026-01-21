"""Tests for Lab 1 Question 3"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q3 import (
    income_tax_fed,
    income_tax_ca,
    income_tax_ma,
    income_tax_ny,
    calculate_income_tax
)

class TestIncomeTaxFed(unittest.TestCase):
    
    def test_income_tax_fed_zero(self):
        result = income_tax_fed(0)
        self.assertEqual(result, 0.0)
    
    def test_income_tax_fed_low_income(self):
        result = income_tax_fed(20000)
        self.assertGreater(result, 0)


class TestIncomeTaxCA(unittest.TestCase):
    
    def test_income_tax_ca_zero(self):
        result = income_tax_ca(0)
        self.assertEqual(result, 0.0)


class TestIncomeTaxMA(unittest.TestCase):
    
    def test_income_tax_ma_flat_rate(self):
        result = income_tax_ma(50000)
        self.assertEqual(result, 2500.0)


class TestIncomeTaxNY(unittest.TestCase):
    
    def test_income_tax_ny_zero(self):
        result = income_tax_ny(0)
        self.assertEqual(result, 0.0)


class TestCalculateIncomeTax(unittest.TestCase):
    
    def test_calculate_income_tax_invalid_state(self):
        inputs = ['TX', '50000']
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                calculate_income_tax()
                self.assertIn("Invalid state", fake_out.getvalue())
    
    def test_calculate_income_tax_valid_ma(self):
        inputs = ['MA', '50000']
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                calculate_income_tax()
                self.assertIn("$50000 before tax", fake_out.getvalue())


if __name__ == '__main__':
    unittest.main()