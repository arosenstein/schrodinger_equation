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
        test = Schrodinger(0.5, -0.5, 50, 1, lambda x: x**3 - 3*x)
        x = test.get_basis()
        self.assertEqual(len(x), 50)

    def test_legendre_basis(self):
        test = Schrodinger(0.5, -.5, 50, 0, lambda x: x)
        x = test.get_basis()
        soln = np.zeros(50)
        soln[1] = 1
        for i in range(len(soln)):
            self.assertTrue(abs(soln[i] - x[i]) <= self.constraint) #Check that there is minimal error

    def test_legendre_hamiltonian(self):
        test = Schrodinger(0.5, -0.5, 50, 0, lambda x: x**3 - 3*x)
        test.get_basis()
        b = test.apply_hamiltonian(test.basis_set)
        self.assertTrue(len(b) != 0)
        valuesAreZero = False
        for i in b:
            valuesAreZero = valuesAreZero and i == 0

        self.assertTrue(not valuesAreZero)


    def test_fourier_hamiltonian(self):
        test = Schrodinger(0.5, -0.5, 50, 1, lambda x: x**3 - 3*x)
        test.get_basis()
        b = test.apply_hamiltonian(test.basis_set)
        self.assertTrue(len(b) != 0)
        valuesAreZero = False
        for i in b:
            valuesAreZero = valuesAreZero and i == 0

        self.assertTrue(not valuesAreZero)

    def test_variation(self):
        test = Schrodinger(0.5, -0.5, 50, 1, lambda x: x**3 - 3*x)
        e_min = test.variation(basis = np.ones(50))
        self.assertTrue(e_min != 0)


    def tearDown(self):

        pass