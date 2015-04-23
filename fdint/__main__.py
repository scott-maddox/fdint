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

# Make sure we import the local package
import os
import sys
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import fdint
from fdint import fdk, dfdk

import numpy
import matplotlib.pyplot as plt

# Plot the available FD integrals and first and second derivatives
_, ax = plt.subplots()
ax.set_xlabel('Normalized Fermi Energy')
ax.set_ylabel('Fermi-Dirac Integrals and Derivatives')
phi = numpy.linspace(-30, 50, 10000)
for k2 in range(-9, 0, 2)+range(0, 22):
    k = k2/2.
    ax.semilogy(phi, fdk(k, phi), 'r')
for k2 in range(-7, 0, 2)+range(2, 22):
    k = k2/2.
    ax.semilogy(phi, dfdk(k, phi), 'b')
for k2 in range(-5, 0, 2)+range(4, 22):
    k = k2/2.
    ax.semilogy(phi, dfdk(k, phi, d=2), 'g')
plt.show()
