#
#   Copyright (c) 2015, Scott J. Maddox
#
#   This file is part of Fermi-Dirac Integrals (FDINT).
#
#   FDINT is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   FDINT is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with FDINT.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
'''
Precise and fast Fermi-Dirac integrals of integer and half integer order.
    
[1] T. Fukushima, "Precise and fast computation of Fermi-Dirac integral
    of integer and half integer order by piecewise minimax rational
    approximation," Applied Mathematics and Computation, vol. 259,
    pp. 708-729, May 2015.
'''
from . import pyfd
try:
    from . import ffd
    _fd = ffd
except Exception as error:
    import sys
    sys.stderr.write('WARNING: Unable to import the fdint fortran module. '
                     'Falling back to the slower python module.\n')
    _fd = pyfd

import numpy

__all__ = ['_fd', 'fdk', 'dfdk']

def fdk(k, phi):
    '''
    Double precision Fermi-Dirac integral of order k.
    
    Parameters
    ----------
    k : int
        Order of the Fermi-Dirac integral.
    phi : float or ndarray
        Normalized Fermi energy above the band edge, i.e. (Ef-Ec)/kT.
    
    Returns
    -------
    value : float or ndarray
        Value of the Fermi-Dirac integral.
    
    Raises
    ------
    NotImplementedError
        If the particular order is not implemented.
    '''
    if isinstance(phi, numpy.ndarray):
        value, err = _fd.vfdk2(int(k*2), phi)
    else:
        value, err = _fd.fdk2(int(k*2), phi)
    if err:
        raise NotImplementedError()
    return value

def dfdk(k, phi, d=1):
    '''
    Double precision derivative of the Fermi-Dirac integral of order k.
    
    Parameters
    ----------
    k : int
        Order of the Fermi-Dirac integral.
    phi : float or ndarray
        Normalized Fermi energy above the band edge, i.e. (Ef-Ec)/kT.
    d : int (default=1)
        Order of dirivative.
    
    Returns
    -------
    value : float or ndarray
        Value of the Fermi-Dirac integral.
    
    Raises
    ------
    NotImplementedError
        If the particular order is not implemented.
    '''
    if isinstance(phi, numpy.ndarray):
        value, err = _fd.vdfdk2(int(k*2), phi, d)
    else:
        value, err = _fd.dfdk2(int(k*2), phi, d)
    if err:
        raise NotImplementedError()
    return value
