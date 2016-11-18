#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_schrodinger_equation
----------------------------------

Tests for `schrodinger_equation` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner
import numpy as np

from schrodinger_equation.schrodinger_equation import *



class TestSchrodinger_equation(unittest.TestCase):

    def setUp(self):
        self.constraint = 0.00001
        pass



    def test_fourier_basis(self):
        pass

    def test_legendre_basis(self):
        test = Schrodinger(0.5, -.5, 50, 0, lambda x: x)
        x = test.get_basis()
        soln = np.zeros(50)
        soln[1] = 1
        for i in range(len(soln)):
            self.assertTrue(abs(soln[i] - x[i]) <= self.constraint) #Check that there is minimal error

    def tearDown(self):

        pass