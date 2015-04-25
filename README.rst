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

First, you will need to install the following prerequisite package::

- Numpy_

.. _`Numpy`: http://docs.scipy.org/doc/numpy/user/install.html

Additional functionality is provided by the following optional packages::

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

Now you can access the Fermi-Dirac integral and derivative convenience
functions, ``fdk`` and ``dfdk``::

    >>> fdk(k=0.5,phi=-10)
    4.0233994366893939e-05
    >>> fdk(0.5,-10)
    4.0233994366893939e-05
    >>> fdk(k=0.5,phi=5)
    7.837976057293096
    >>> fdk(k=0.5,phi=50)
    235.81861512588432
    >>> dfdk(k=0.5,phi=-10,d=1) # first derivative
    4.0233348580568672e-05
    >>> dfdk(k=0.5,phi=5,d=1)
    2.1916282173557855
    >>> dfdk(k=0.5,phi=50,d=1)
    7.0699026455055112
    >>> dfdk(k=0.5,phi=50,d=2) # second derivative
    0.07074571454521902

You can also pass in lists or arrays as phi::

    >>> fdk(k=0.5,phi=[-10,0,10])
    array([  4.02339944e-05,   6.78093895e-01,   2.13444715e+01])

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

If you prefer to call the low-level functions directly to avoid overhead,
you can access them from the ``fd`` module::

    >>> fd.fd1h(-10) # k=1/2
    4.023399436689394e-05
    >>> fd.vfd1h([-10,0,10]) # k=1/2
    array([  4.02339944e-05,   6.78093895e-01,   2.13444715e+01])

Benchmarks
==========

For single values, calling the function for a specific order is ~7x faster than
calling ``fdk``::

    $ python -m timeit -s "from fdint import fdk" "fdk(0.5, 10)"
    1000000 loops, best of 3: 1.1 usec per loop
    $ python -m timeit -s "from fdint.fd import fd1h" "fd1h(10)"
    10000000 loops, best of 3: 0.153 usec per loop

However, even for a fairly small array of 1000, most of the advantage is lost::

    $ python -m timeit -s "from fdint import fdk; import numpy; x=numpy.linspace(-100,100,1000)" "fdk(0.5, x)"
    100000 loops, best of 3: 13.8 usec per loop
    $ python -m timeit -s "from fdint.fd import vfd1h; import numpy; x=numpy.linspace(-100,100,1000)" "vfd1h(x)"
    100000 loops, best of 3: 12.9 usec per loop

Overall, the performance is excellent. Note that the call time is within a
factor of 2 of ``numpy.exp``.

    $ python -m timeit -s "import numpy; from numpy import exp; x=numpy.linspace(-100,100,1000)" "exp(x)"
    100000 loops, best of 3: 7.49 usec per loop

Documentation
=============

The `documentation`_ (coming soon) is graciously hosted by GitHub.