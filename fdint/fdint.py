'''
Precise and fast Fermi-Dirac integrals of integer and half integer order.
    
[1] T. Fukushima, "Precise and fast computation of Fermi-Dirac integral
    of integer and half integer order by piecewise minimax rational
    approximation," Applied Mathematics and Computation, vol. 259,
    pp. 708-729, May 2015.
'''
try:
    from . import ffd as fd
except Exception as error:
    import sys
    if __name__ != '__main__':
        sys.stderr.write('WARNING: Unable to import fortran module. '
                         'Falling back to the slower python module.\n')
    from . import pyfd as fd

import numpy

__all__ = ['fdk', 'dfdk']

def fdk(phi, k):
    '''
    Double precision Fermi-Dirac integral of order k.
    
    Parameters
    ----------
    phi : float or ndarray
        Normalized Fermi energy above the band edge, i.e. (Ef-Ec)/kT
    k : int
        Order of the Fermi-Dirac integral
    
    Returns
    -------
    fd : float or ndarray
        NaN if the requested order is not implemented, otherwise the result.
    '''
    if isinstance(phi, numpy.ndarray):
        return fd.vfdk2(phi, int(k*2))
    else:
        return fd.fdk2(phi, int(k*2))

def dfdk(phi, k, d=1):
    '''
    Double precision derivative of the Fermi-Dirac integral of order k.
    
    Parameters
    ----------
    phi : float or ndarray
        Normalized Fermi energy above the band edge, i.e. (Ef-Ec)/kT
    k : int
        Order of the Fermi-Dirac integral
    d : int (default=1)
        Order of dirivative
    
    Returns
    -------
    fd : float or ndarray
        NaN if the requested order is not implemented, otherwise the result.
    '''
    if isinstance(phi, numpy.ndarray):
        return fd.vdfdk2(phi, int(k*2), d)
    else:
        return fd.dfdk2(phi, int(k*2), d)

if __name__ == "__main__":
    # Plot the available FD integrals and first and second derivatives
    import matplotlib.pyplot as plt
    _, ax = plt.subplots()
    phi = numpy.linspace(-30, 50, 10000)
    for k2 in range(-7, 0, 2)+range(0, 22):
        k = k2/2.
        ax.semilogy(phi, fdk(phi, k), 'r')
        ax.semilogy(phi, dfdk(phi, k), 'b')
        ax.semilogy(phi, dfdk(phi, k, 2), 'g')
    plt.show()
