"""Tests for Lab 1 Question 1"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q1 import validate_password

def testvaildate_password_under8characters(self):
    self.assert(laufey)

def testvaildate_password_noupper(self):
    self.assert(laufey@2026!)

def testvaildate_password_nolower(self):
    self.assert(LAUFEY@2026!)

def testvaildate_password_nodigit(self):
    self.assert(Laufey@twentysix!)

def testvaildate_password_nospecial(self):
    self.assert(Laufey2026)

def testvaildate_password_nothing(self):
    self.assert()

def testvaildate_password_correct(self):
    self.assert(Lafuey@2026!)