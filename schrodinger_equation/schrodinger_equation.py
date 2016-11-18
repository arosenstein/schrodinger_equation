# -*- coding: utf-8 -*-
import numpy as np

class Schrodinger:

	def __init__(self, V0, c, basis_size, basis_function, fxn):
		'''Creates a system to calculate the schrodinger equation

		Args:
        
        	V0 (float): Initial Potential Energy
        	c (float): Constant to be used in Schrodinger equation
            basis_size (int): Size of the basis set
        	basis_function (int): Determines which basis function to use
        		- 0 : Legendre Polynomial
        		- 1 : Fourier Series
        	func (array-like): x and y values corresponding to function values
		'''
		self.V0 = V0
		self.c = c
		self.basis_size = basis_size
		self.basis_function = basis_function
		self.fxn = fxn
		self.x = np.linspace(0,2,2000)

	def get_basis(self):
		'''Determines basis set coefficients for the given wavefunction
		'''

		
		if self.basis_function == 0:
			return np.polynomial.legendre.legfit(self.x, self.fxn(self.x), self.basis_size - 1)
		
		elif self.basis_function == 1:
			return np.array([self._cn(self.fxn, i) for i in range(self.basis_size)])

		else:
			return None

	def _cn(self, fxn, n):
		l = abs(self.x[0] - self.x[-1])
		c = self.fxn(x) * np.exp(-2j * n * np.pi * self.x / l)
		return c.sum()/c.size()




