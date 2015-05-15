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
    
[1] T. Fukushima, "Precise and fast computation of Fermi-Dirac integral of
    integer and half integer order by piecewise minimax rational approximation,"
    Applied Mathematics and Computation, vol. 259, pp. 708-729, May 2015.
    DOI: 10.1016/j.amc.2015.03.009
'''

from .version import __version__

from . import _fdint

from .fd import *

def fdk(k, phi):
    k2 = str(int(k*2.01)).replace('-', 'm')
    funcname = 'fd'+k2+'h'
    if funcname not in globals():
        raise NotImplementedError()
    func = globals()[funcname]
    return func(phi)

del version