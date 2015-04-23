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

This is the easiest method. Install from `PyPi`_ by running the following
command::

    pip install fdint

.. _`PyPi`: http://pypi.python.org/pypi

From Github
-----------

First, you will need to install the following prerequisite packages:

- Numpy_

.. _`Numpy`: http://docs.scipy.org/doc/numpy/user/install.html

Additional functionality is provided by the following optional packages:

- Matplotlib_

.. _`Matplotlib`: http://matplotlib.org/users/installing.html

Once these are installed, download the latest release `.zip` or `.tar.gz`
source package from the `github page`_, extract its contents, and run
`python setup.py install` from within the extracted directory.

.. _`github page`: http://github.com/scott-maddox/fdint/releases/latest

Testing
=======

Once installed, you can test the package by running the following command::

    python -m fdint.tests

If you have Matplotlib_ installed, you can also plot a sample of the available
functions by running the following command::

    python -m fdint

Tutorial
========

First, start up an interactive python shell from the command line::

    $ python

Next, import everything from the ``fdint`` package::

    >>> from fdint import *

If you see the following warning, then the Fortran library failed to compile
and/or install::

    WARNING: Unable to import fortran module. Falling back to the slower python
    module.

The same functionality is provided by the fall-back python module, but
the python module is considerably slower. Either way, now you can access the
Fermi-Dirac integral, ``fdk``, and  the derivative, ``dfdk``, convenience
functions::

    >>> fdk(k=0.5,phi=-10)
    4.0233994366893939e-05
    >>> fdk(0.5,-10)
    4.0233994366893939e-05
    >>> fdk(k=0.5,phi=5)
    7.837976057293096
    >>> fdk(k=0.5,phi=50)
    235.81861512588432
    >>> dfdk(k=0.5,phi=-10,d=1)
    4.0233348580568672e-05
    >>> dfdk(k=0.5,phi=5,d=1)
    2.1916282173557855
    >>> dfdk(k=0.5,phi=50,d=1)
    7.0699026455055112
    >>> dfdk(k=0.5,phi=50,d=2)
    0.07074571454521902

If you request an order or derivative that is not implemented, a
NotImplementedError is raised::

    >>> fdk(22,0)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "fdint/fdint.py", line 68, in fdk
        raise NotImplementedError()
    NotImplementedError
    >>> dfdk(k=0.5,phi=50,d=10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "fdint/fdint.py", line 99, in dfdk
        raise NotImplementedError()
    NotImplementedError

If you prefer to call the low-level functions directly, you can access them
from the ``_fd`` module::

    >>> _fd.fd1h(-10)
    4.0233994366893939e-05

Documentation
=============

The `documentation`_ (coming soon) is graciously hosted by GitHub.

.. _`documentation`: http://scott-maddox.github.io/fdint