===============================
Schrodinger Equation
===============================


.. image:: https://travis-ci.org/arosenstein/schrodinger_equation.svg?branch=master
    :target: https://travis-ci.org/arosenstein/schrodinger_equation

.. image:: https://pyup.io/repos/github/arosenstein/schrodinger_equation/shield.svg
     :target: https://pyup.io/repos/github/arosenstein/schrodinger_equation/
     :alt: Updates


Schrodinger Equation solver


* Free software: MIT license
* Documentation: https://schrodinger-equation.readthedocs.io.


Features
--------

* This program solves the Schrodinger Equation by approximating wave functions with both legendre polynomials and fourier series.

* Also uses the variational principle to minimize energy of the system given constraints.

How to Use
--------
* In order to run, all of the information goes in the constructor of the ``Schrodinger`` class. It takes in the following parameters:
  - Initial Potential Energy
  - Constant to be used in the Schrodinger Equation
  - Size of the basis set (number of terms in approximation)
  - Which approximation method to use for the wavefunction
  - Wavefunction

Constructor examples can be found in the tests.

TODO
--------
* Add alternative ways to approximate wave functions 

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

