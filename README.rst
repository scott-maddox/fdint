Fermi-Dirac Integrals (FDINT)
=============================

Precise and fast Fermi-Dirac integrals of integer and half integer order.
    
[1] T. Fukushima, "Precise and fast computation of Fermi-Dirac integral
    of integer and half integer order by piecewise minimax rational
    approximation," Applied Mathematics and Computation, vol. 259,
    pp. 708-729, May 2015.

The `source code`_ and `documentation`_ (coming soon) are graciously hosted
by GitHub.

.. _`source code`: http://github.com/scott-maddox/fdint
.. _`documentation`: http://scott-maddox.github.io/fdint


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


Documentation
=============

Once you have OBPDS installed, check out the `tutorial`_
(coming soon) and `documentation`_ (coming soon) to get acquainted.

.. _`tutorial`: http://scott-maddox.github.io/fdint/tutorial
.. _`documentation`: http://scott-maddox.github.io/fdint