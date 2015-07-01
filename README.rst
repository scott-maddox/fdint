Fermi-Dirac Integrals (FDINT)
=============================

FDINT is a free, open-source python package that provides fast, double
precision (64-bit floating point) approximations to the Fermi-Dirac
integrals of integer and half integer order, based on the work by
Prof. Fukushima [1-3]. FDINT is written predominantly in Cython_, which
is compiled to native code through an intermediate C source, resulting
in C-like performance.

.. [1] T. Fukushima, "Precise and fast computation of Fermi-Dirac integral of
   integer and half integer order by piecewise minimax rational approximation,"
   Applied Mathematics and Computation, vol. 259, pp. 708-729, May 2015.
   DOI: 10.1016/j.amc.2015.03.009

.. [2] T. Fukushima, "Precise and fast computation of inverse Fermi-Dirac
   integral of order 1/2 by minimax rational function approximation,"
   Applied Mathematics and Computation, vol. 259, pp. 698-707, May 2015.
   DOI: 10.1016/j.amc.2015.03.015
    
.. [3] T. Fukushima, "Precise and fast computation of generalized Fermi-Dirac
   integral by parameter polynomial approximation," 2014.
   DOI: 10.13140/2.1.1094.6566

The `source code`_ and `documentation`_ (coming soon) are graciously hosted
by GitHub.

Installation
============

In order to use FDINT, you must have a working `Python`_ distribution
installed. Python 3 support has not yet been tested, so Python 2.7 is
suggested. You will also need to install `Numpy`_ before proceeding. If
you're not familiar with Python, you might consider installing a
`Python distribution`_ that comes prepackaged with Numpy.

From PyPi
---------

This is the recommended method for installing FDINT. `PyPi`_ is the python
package index, which contains many python packages that can be easily installed
with a single command. To install FDINT from `PyPi`_, open up a command
prompt and run the following command::

    pip install fdint


From Github
-----------

To install the latest release of FDINT from Github, go to the
`FDINT releases page`_, download the latest ``.zip`` or ``.tar.gz``
source package, extract its contents, and run ``python setup.py install``
from within the extracted directory.


Testing
=======

Once installed, you can test the package by running the following command::

    python -m fdint.tests

If you have Matplotlib_ installed, you can also plot a sample of the
available functions by running the following command::

    python -m fdint.examples.plot

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
    >>> dfdk(k=0.5,phi=-10) # first derivative
    4.0233348580568672e-05

You can also pass in numpy arrays as phi::

    >>> import numpy
    >>> fdk(k=0.5,phi=numpy.linspace(-100,10,3))
    array([  3.29683149e-44,   2.53684104e-20,   2.13444715e+01])

If you request an order or derivative that is not implemented, a
NotImplementedError is raised::

    >>> fdk(1,0)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "fdint/__init__.py", line 50, in fdk
        raise NotImplementedError()
    NotImplementedError

For semiconductor calculations, ``parabolic``, ``dparabolic``, ``iparabolic``,
``nonparabolic``, and ``dnonparabolic`` are provided::

    >>> parabolic(0)
    0.7651470246254078
    >>> dparabolic(0)
    0.6048986434216304
    >>> iparabolic(.7)
    -0.11156326391089397
    >>> nonparabolic(0,0)
    0.7651470705342294
    >>> nonparabolic(0,0.07) # InAs
    1.006986898726782
    >>> dnonparabolic(0,0.07) # InAs
    0.8190058991462952

Benchmarks
==========

Below are a few benchmarking runs. First, ``numpy.exp``::

    $ python -m timeit -s "import numpy; from numpy import exp; x=numpy.linspace(-100,10,10000)" "exp(x)"
    10000 loops, best of 3: 72.6 usec per loop

The same arguments to the Fermi-Dirac integral of order k=1/2, ``fdint.fd1h``,
takes only ~2.2x the runtime::

    $ python -m timeit -s "from fdint import fd1h; import numpy; x=numpy.linspace(-100,10,10000)" "fd1h(x)"
    10000 loops, best of 3: 158 usec per loop

Similarly, the inverse Fermi-Dirac integral of order k=1/2, ``fdint.ifd1h``,
takes only ~2.4x the runtime of ``numpy.log``::

    $ python -m timeit -s "import numpy; from numpy import exp,log; x=numpy.linspace(-100,10,10000);y=exp(x)" "log(y)"
    10000 loops, best of 3: 69.9 usec per loop
    $ python -m timeit -s "from fdint import fd1h,ifd1h; import numpy; x=numpy.linspace(-100,10,10000);y=fd1h(x)" "ifd1h(y)"
    10000 loops, best of 3: 178 usec per loop
    
The generalized Fermi-Dirac integrals are also quite fast. For order
k=1/2 with zero nonparabolicity, ``fdint.gfd1h`` takes only ~3.7x the runtime
of ``numpy.exp`` for zero nonparabolicity::

    $ python -m timeit -s "from fdint import gfd1h; import numpy; x=numpy.linspace(-100,10,10000);b=numpy.zeros(10000);b.fill(0.)" "gfd1h(x,b)"
    1000 loops, best of 3: 266 usec per loop

However, if there is significant nonparabolicity, ``fdint.gfd1h`` can take a
up to ~10x longer than ``numpy.exp``::

    $ python -m timeit -s "from fdint import gfd1h; import numpy; x=numpy.linspace(-100,10,10000);b=numpy.zeros(10000);b.fill(0.1)" "gfd1h(x,b)"
    1000 loops, best of 3: 467 usec per loop

    $ python -m timeit -s "from fdint import gfd1h; import numpy; x=numpy.linspace(-100,10,10000);b=numpy.zeros(10000);b.fill(0.3)" "gfd1h(x,b)"
    /usr/local/Cellar/python/2.7.8_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/timeit.py:6: RuntimeWarning: gfd1h: less than 24 bits of accuracy
    1000 loops, best of 3: 696 usec per loop

The full calculation for a nonparabolic band takes ~5-17x longer than
``numpy.exp``, depending on the level of nonparabolicity (Note: for
some reason the timing for this command is unreasonably high when timed
from the command line. When timed inside of ipython, it works fine)::

    $ ipython
    In [1]: from fdint import *
    
    In [2]: import numpy
    
    In [3]: phi = numpy.linspace(-100,10,10000)
    
    In [4]: %timeit numpy.exp(phi)
    10000 loops, best of 3: 72.9 µs per loop
    
    In [5]: %timeit parabolic(phi)
    10000 loops, best of 3: 165 µs per loop
    
    In [6]: alpha = numpy.empty(10000); alpha.fill(0.0) # parabolic
    
    In [7]: %timeit nonparabolic(phi, alpha)
    1000 loops, best of 3: 346 µs per loop
    
    In [8]: alpha = numpy.empty(10000); alpha.fill(0.07) # InAs
    
    In [9]: %timeit nonparabolic(phi, alpha)
    1000 loops, best of 3: 695 µs per loop
    
    In [10]: alpha = numpy.empty(10000); alpha.fill(0.15) # InSb
    
    In [11]: %timeit nonparabolic(phi, alpha)
    /usr/local/bin/ipython:257: RuntimeWarning: nonparabolic: less than 24 bits of accuracy
    1000 loops, best of 3: 1.26 ms per loop

Documentation
=============

The `documentation`_ (coming soon) is graciously hosted by GitHub.

.. _`source code`: http://github.com/scott-maddox/fdint
.. _`documentation`: http://scott-maddox.github.io/fdint
.. _`PyPi`: http://pypi.python.org/pypi
.. _`Python`: https://www.python.org/download/
.. _`Cython`: http://docs.cython.org/src/quickstart/install.html
.. _`Numpy`: http://docs.scipy.org/doc/numpy/user/install.html
.. _`matplotlib`: http://matplotlib.org/users/installing.html
.. _`Python distribution`: https://www.scipy.org/install.html#scientific-python-distributions
.. _`FDINT releases page`: http://github.com/scott-maddox/fdint/releases/latest