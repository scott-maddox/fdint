Fermi-Dirac Integrals (FDINT)
=============================

FDINT is a free, open-source python package that provides fast, double
precision (64-bit floating point) approximations to the Fermi-Dirac
integrals of integer and half integer order, based on the work by
Prof. Fukushima [1].
    
.. [1] T. Fukushima, "Precise and fast computation of Fermi-Dirac integral
   of integer and half integer order by piecewise minimax rational
   approximation," Applied Mathematics and Computation, vol. 259,
   pp. 708-729, May 2015.

Installation
============

In order to use FDINT, you must having a working `Python`_ distribution
installed. Python 3 support has not yet been tested, so Python 2.7 is
suggested. In order to achieve the highest performance, a Fortran 90 compiler,
such as gfortran, is required.

.. _`Python`: https://www.python.org/download/

From PyPi
---------

This is the easiest method. Install from `PyPi`_ by running `pip install fdint`
from the command line.

.. _`PyPi`: http://pypi.python.org/pypi

From Github
-----------

First, you will need to install the following prerequisite packages:

- Numpy_

.. _`Numpy`: http://docs.scipy.org/doc/numpy/user/install.html

Additional funcitonality is provided by the following optional packages:

- Matplotlib_

.. _`Matplotlib`: http://matplotlib.org/users/installing.html

Once these are installed, download the latest release `.zip` or `.tar.gz`
source package from the `github page`_, extract its contents, and run
`python setup.py install` from within the extracted directory.

.. _`github page`: http://github.com/scott-maddox/obpds/releases/latest

Testing
=======

You can test the installation by running `python -m fdint.tests`.