# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
'''
Precise and fast Fermi-Dirac integrals of integer and half integer order.
    
[1] T. Fukushima, "Precise and fast computation of Fermi-Dirac integral of
    integer and half integer order by piecewise minimax rational approximation,"
    Applied Mathematics and Computation, vol. 259, pp. 708-729, May 2015.
    DOI: 10.1016/j.amc.2015.03.009

[2] T. Fukushima, "Precise and fast computation of inverse Fermi-Dirac
    integral of order 1/2 by minimax rational function approximation,"
    Applied Mathematics and Computation, vol. 259, pp. 698-707, May 2015.
    DOI: 10.1016/j.amc.2015.03.015
    
[3] T. Fukushima, "Precise and fast computation of generalized Fermi-Dirac
    integral by parameter polynomial approximation," 2014.
    DOI: 10.13140/2.1.1094.6566
'''

from .version import __version__

def get_include():
    """
    Return the directory that contains the FDINT \\*.pxd files.
    Cython extension modules that need to compile against FDINT should use
    this function to locate the appropriate include directory.
    Notes
    -----
    When using ``distutils``, for example in ``setup.py``.
    ::
        import fdint
        ...
        Extension('extension_name', ...
                  include_dirs=[fdint.get_include()])
        ...
    """
    import fdint
    return os.path.dirname(fdint.__file__)

from . import _fdint

from .fd import *
from .dfd import *
from .ifd import *
from .gfd import *
from .dgfd import *
from .scfd import *

def fdk(k, phi):
    k2 = str(int(k*2.01)).replace('-', 'm')
    funcname = 'fd'+k2+'h'
    if funcname not in globals():
        raise NotImplementedError()
    func = globals()[funcname]
    return func(phi)

def dfdk(k, phi):
    k2 = str(int(k*2.01)).replace('-', 'm')
    funcname = 'dfd'+k2+'h'
    if funcname not in globals():
        raise NotImplementedError()
    func = globals()[funcname]
    return func(phi)

def ifdk(k, nu):
    k2 = str(int(k*2.01)).replace('-', 'm')
    funcname = 'ifd'+k2+'h'
    if funcname not in globals():
        raise NotImplementedError()
    func = globals()[funcname]
    return func(nu)

def gfdk(k, phi, alpha):
    k2 = str(int(k*2.01)).replace('-', 'm')
    funcname = 'gfd'+k2+'h'
    if funcname not in globals():
        raise NotImplementedError()
    func = globals()[funcname]
    return func(phi, alpha)

def dgfdk(k, phi, alpha):
    k2 = str(int(k*2.01)).replace('-', 'm')
    funcname = 'dgfd'+k2+'h'
    if funcname not in globals():
        raise NotImplementedError()
    func = globals()[funcname]
    return func(phi, alpha)

del version