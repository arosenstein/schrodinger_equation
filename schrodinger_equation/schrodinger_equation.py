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
        	fxn (array-like): x and y values corresponding to function values
		'''
		self.V0 = V0
		self.c = c
		self.basis_size = basis_size
		self.basis_function = basis_function
		self.fxn = fxn
		self.x = np.linspace(0,2,2000)
		self.l = abs(self.x[0] - self.x[-1])

	def get_basis(self):
		'''Determines basis set coefficients for the given wavefunction
		'''

		
		if self.basis_function == 0:
			self.basis_set = np.polynomial.legendre.legfit(self.x, self.fxn(self.x), self.basis_size - 1)
		
		elif self.basis_function == 1:
			self.basis_set = np.array([self._cn(self.fxn, i) for i in range(self.basis_size)])

		else:
			self.basis_set = None

		return self.basis_set

	def _cn(self, fxn, n):
		l = abs(self.x[0] - self.x[-1])
		c = self.fxn(self.x) * np.exp(-2j * n * np.pi * self.x / l)
		return sum(c)/len(c)

	def apply_hamiltonian(self):

		if self.basis_function == 0:
			temp = np.polynomial.legendre.legder(self.basis_set, 2)
			d_2 = np.zeros(len(temp) + 2)
			for i in range(len(temp)):
				d_2[i] = temp[i]
			self.converted_basis = -self.c * d_2 + self.V0 * self.basis_set * self.l

		elif self.basis_function == 1:
			H = np.zeros([self.basis_size, self.basis_size])
			for i in range(self.basis_size):
				H[i][i] = (-4 * (i**2) * (np.pi ** 2) / self.l)
			self.converted_basis = H.dot(self.basis_set)

		else:
			self.converted_basis = None

		return self.converted_basis





