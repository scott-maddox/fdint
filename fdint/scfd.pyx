# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
'''
Semiconductor Fermi-Dirac integrals
'''
cimport cython
from libc.math cimport exp, log
cimport numpy as np
from fdint cimport _fdint
import numpy

DEF SQRT_PI_2 = 0.88622692545275794 # sqrt(pi)/2
DEF INV_SQRT_PI_2 = 1.1283791670955126 # 2/sqrt(pi)

@cython.cdivision(True)
cdef inline double _boltzmann(double phi):
    return exp(phi)

@cython.cdivision(True)
cdef inline double _dboltzmann(double phi):
    return exp(phi)

@cython.cdivision(True)
cdef inline double _iboltzmann(double nu):
    return log(nu)

@cython.cdivision(True)
cdef inline double _parabolic(double phi):
    return _fdint.fd1h(phi)*INV_SQRT_PI_2

@cython.cdivision(True)
cdef inline double _dparabolic(double phi):
    return _fdint.dfd1h(phi)*INV_SQRT_PI_2

@cython.cdivision(True)
cdef inline double _iparabolic(double nu):
    return _fdint.ifd1h(nu*SQRT_PI_2)

@cython.cdivision(True)
cdef inline double _nonparabolic(double phi, double alpha):
    return _fdint.nonparabolic(phi, alpha)*INV_SQRT_PI_2

@cython.cdivision(True)
cdef inline double _dnonparabolic(double phi, double alpha):
    return _fdint.dnonparabolic(phi, alpha)*INV_SQRT_PI_2


@cython.cdivision(True)
cdef inline double _boltzmann_p(double phi, double psi, double E, double N,
                                double Vt):
    return _boltzmann(((E-psi)-phi)/Vt)*N

@cython.cdivision(True)
cdef inline double _boltzmann_n(double phi, double psi, double E, double N,
                                double Vt):
    return _boltzmann((phi-(E-psi))/Vt)*N

@cython.cdivision(True)
cdef inline double _boltzmann_dp(double phi, double psi, double E, double N,
                                 double Vt):
    return -_dboltzmann(((E-psi)-phi)/Vt)*N/Vt

@cython.cdivision(True)
cdef inline double _boltzmann_dn(double phi, double psi, double E, double N,
                                 double Vt):
    return _dboltzmann((phi-(E-psi))/Vt)*N/Vt

@cython.cdivision(True)
cdef inline double _iboltzmann_p(double n, double psi, double E, double N,
                                 double Vt):
    return (E-psi) - _iboltzmann(n / N)*Vt

@cython.cdivision(True)
cdef inline double _iboltzmann_n(double n, double psi, double E, double N,
                                 double Vt):
    return (E-psi) + _iboltzmann(n / N)*Vt

@cython.cdivision(True)
cdef inline double _parabolic_p(double phi, double psi, double E, double N,
                                double Vt):
    return _parabolic(((E-psi)-phi)/Vt)*N

@cython.cdivision(True)
cdef inline double _parabolic_n(double phi, double psi, double E, double N,
                                double Vt):
    return _parabolic((phi-(E-psi))/Vt)*N

@cython.cdivision(True)
cdef inline double _parabolic_dp(double phi, double psi, double E, double N,
                                 double Vt):
    return -_dparabolic(((E-psi)-phi)/Vt)*N/Vt

@cython.cdivision(True)
cdef inline double _parabolic_dn(double phi, double psi, double E, double N,
                                 double Vt):
    return _dparabolic((phi-(E-psi))/Vt)*N/Vt

@cython.cdivision(True)
cdef inline double _iparabolic_p(double n, double psi, double E, double N,
                                 double Vt):
    return (E-psi) - _iparabolic(n / N)*Vt

@cython.cdivision(True)
cdef inline double _iparabolic_n(double n, double psi, double E, double N,
                                 double Vt):
    return (E-psi) + _iparabolic(n / N)*Vt

@cython.cdivision(True)
cdef inline double _nonparabolic_n(double phi, double psi, double alpha,
                                   double E, double N, double Vt):
    return _nonparabolic((phi-(E-psi))/Vt, alpha)*N

@cython.cdivision(True)
cdef inline double _nonparabolic_dn(double phi, double psi, double alpha,
                                    double E, double N, double Vt):
    return _dnonparabolic((phi-(E-psi))/Vt, alpha)*N/Vt

@cython.cdivision(True)
cdef inline double _boltzmann_n3(double phi, double psi,
                                    double E1, double E2, double E3,
                                    double N1, double N2, double N3,
                                    double Vt):
    return ( _boltzmann((phi-(E1-psi))/Vt)*N1
            +_boltzmann((phi-(E2-psi))/Vt)*N2
            +_boltzmann((phi-(E3-psi))/Vt)*N3)

@cython.cdivision(True)
cdef inline double _boltzmann_dn3(double phi, double psi,
                                     double E1, double E2, double E3,
                                     double N1, double N2, double N3,
                                     double Vt):
    return ( _dboltzmann((phi-(E1-psi))/Vt)*N1/Vt
            +_dboltzmann((phi-(E2-psi))/Vt)*N2/Vt
            +_dboltzmann((phi-(E3-psi))/Vt)*N3/Vt)

@cython.cdivision(True)
cdef inline double _parabolic_n3(double phi, double psi,
                                    double E1, double E2, double E3,
                                    double N1, double N2, double N3,
                                    double Vt):
    return ( _parabolic((phi-(E1-psi))/Vt)*N1
            +_parabolic((phi-(E2-psi))/Vt)*N2
            +_parabolic((phi-(E3-psi))/Vt)*N3)

@cython.cdivision(True)
cdef inline double _parabolic_dn3(double phi, double psi,
                                     double E1, double E2, double E3,
                                     double N1, double N2, double N3,
                                     double Vt):
    return ( _dparabolic((phi-(E1-psi))/Vt)*N1/Vt
            +_dparabolic((phi-(E2-psi))/Vt)*N2/Vt
            +_dparabolic((phi-(E3-psi))/Vt)*N3/Vt)

@cython.cdivision(True)
cdef inline double _nonparabolic_n3(double phi, double psi, double alpha,
                                    double E1, double E2, double E3,
                                    double N1, double N2, double N3,
                                    double Vt):
    return (_nonparabolic((phi-(E1-psi))/Vt, alpha)*N1
            +_parabolic((phi-(E2-psi))/Vt)*N2
            +_parabolic((phi-(E3-psi))/Vt)*N3)

@cython.cdivision(True)
cdef inline double _nonparabolic_dn3(double phi, double psi, double alpha,
                                     double E1, double E2, double E3,
                                     double N1, double N2, double N3,
                                     double Vt):
    return (_dnonparabolic((phi-(E1-psi))/Vt, alpha)*N1/Vt
            +_dparabolic((phi-(E2-psi))/Vt)*N2/Vt
            +_dparabolic((phi-(E3-psi))/Vt)*N3/Vt)
 
 
@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vboltzmann(np.ndarray[double] phi,
                      np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _boltzmann(phi[i])

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vdboltzmann(np.ndarray[double] phi,
                       np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _dboltzmann(phi[i])

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _viboltzmann(np.ndarray[double] phi,
                       np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _iboltzmann(phi[i])
 
@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vparabolic(np.ndarray[double] phi,
                      np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _parabolic(phi[i])

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vdparabolic(np.ndarray[double] phi,
                       np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _dparabolic(phi[i])

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _viparabolic(np.ndarray[double] phi,
                       np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _iparabolic(phi[i])
 
@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vnonparabolic(np.ndarray[double] phi,
                         np.ndarray[double] alpha,
                         np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _nonparabolic(phi[i], alpha[i])

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vdnonparabolic(np.ndarray[double] phi,
                          np.ndarray[double] alpha,
                          np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _dnonparabolic(phi[i], alpha[i])


@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vboltzmann_p(np.ndarray[double] phi,
                        np.ndarray[double] psi,
                        np.ndarray[double] E,
                        np.ndarray[double] N,
                        double Vt,
                        np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _boltzmann_p(phi[i], psi[i], E[i], N[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vboltzmann_n(np.ndarray[double] phi,
                        np.ndarray[double] psi,
                        np.ndarray[double] E,
                        np.ndarray[double] N,
                        double Vt,
                        np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _boltzmann_n(phi[i], psi[i], E[i], N[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vboltzmann_dp(np.ndarray[double] phi,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                        double Vt,
                        np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _boltzmann_dp(phi[i], psi[i], E[i], N[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vboltzmann_dn(np.ndarray[double] phi,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                         double Vt,
                         np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _boltzmann_dn(phi[i], psi[i], E[i], N[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _viboltzmann_p(np.ndarray[double] n,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                         double Vt,
                         np.ndarray[double] out):
    cdef int num = n.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _iboltzmann_p(n[i], psi[i], E[i], N[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _viboltzmann_n(np.ndarray[double] n,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                         double Vt,
                         np.ndarray[double] out):
    cdef int num = n.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _iboltzmann_n(n[i], psi[i], E[i], N[i], Vt)
 

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vparabolic_p(np.ndarray[double] phi,
                        np.ndarray[double] psi,
                        np.ndarray[double] E,
                        np.ndarray[double] N,
                        double Vt,
                        np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _parabolic_p(phi[i], psi[i], E[i], N[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vparabolic_n(np.ndarray[double] phi,
                        np.ndarray[double] psi,
                        np.ndarray[double] E,
                        np.ndarray[double] N,
                        double Vt,
                        np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _parabolic_n(phi[i], psi[i], E[i], N[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vparabolic_dp(np.ndarray[double] phi,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                         double Vt,
                         np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _parabolic_dp(phi[i], psi[i], E[i], N[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vparabolic_dn(np.ndarray[double] phi,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                         double Vt,
                         np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _parabolic_dn(phi[i], psi[i], E[i], N[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _viparabolic_p(np.ndarray[double] n,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                         double Vt,
                         np.ndarray[double] out):
    cdef int num = n.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _iparabolic_p(n[i], psi[i], E[i], N[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _viparabolic_n(np.ndarray[double] n,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                         double Vt,
                         np.ndarray[double] out):
    cdef int num = n.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _iparabolic_n(n[i], psi[i], E[i], N[i], Vt)


@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vnonparabolic_n(np.ndarray[double] phi,
                           np.ndarray[double] psi,
                           np.ndarray[double] alpha,
                           np.ndarray[double] E,
                           np.ndarray[double] N,
                           double Vt,
                           np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _nonparabolic_n(phi[i], psi[i], alpha[i], E[i], N[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vnonparabolic_dn(np.ndarray[double] phi,
                            np.ndarray[double] psi,
                            np.ndarray[double] alpha,
                            np.ndarray[double] E,
                            np.ndarray[double] N,
                            double Vt,
                            np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _nonparabolic_dn(phi[i], psi[i], alpha[i], E[i], N[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vboltzmann_n3(np.ndarray[double] phi,
                         np.ndarray[double] psi,
                         np.ndarray[double] E1,
                         np.ndarray[double] E2,
                         np.ndarray[double] E3,
                         np.ndarray[double] N1,
                         np.ndarray[double] N2,
                         np.ndarray[double] N3,
                         double Vt,
                         np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _boltzmann_n3(phi[i], psi[i],
                               E1[i], E2[i], E3[i],
                               N1[i], N2[i], N3[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vboltzmann_dn3(np.ndarray[double] phi,
                          np.ndarray[double] psi,
                          np.ndarray[double] E1,
                          np.ndarray[double] E2,
                          np.ndarray[double] E3,
                          np.ndarray[double] N1,
                          np.ndarray[double] N2,
                          np.ndarray[double] N3,
                          double Vt,
                          np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _boltzmann_dn3(phi[i], psi[i],
                                E1[i], E2[i], E3[i],
                                N1[i], N2[i], N3[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vparabolic_n3(np.ndarray[double] phi,
                         np.ndarray[double] psi,
                         np.ndarray[double] E1,
                         np.ndarray[double] E2,
                         np.ndarray[double] E3,
                         np.ndarray[double] N1,
                         np.ndarray[double] N2,
                         np.ndarray[double] N3,
                         double Vt,
                         np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _parabolic_n3(phi[i], psi[i],
                               E1[i], E2[i], E3[i],
                               N1[i], N2[i], N3[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vparabolic_dn3(np.ndarray[double] phi,
                          np.ndarray[double] psi,
                          np.ndarray[double] E1,
                          np.ndarray[double] E2,
                          np.ndarray[double] E3,
                          np.ndarray[double] N1,
                          np.ndarray[double] N2,
                          np.ndarray[double] N3,
                          double Vt,
                          np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _parabolic_dn3(phi[i], psi[i],
                                E1[i], E2[i], E3[i],
                                N1[i], N2[i], N3[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vnonparabolic_n3(np.ndarray[double] phi,
                            np.ndarray[double] psi,
                            np.ndarray[double] alpha,
                            np.ndarray[double] E1,
                            np.ndarray[double] E2,
                            np.ndarray[double] E3,
                            np.ndarray[double] N1,
                            np.ndarray[double] N2,
                            np.ndarray[double] N3,
                            double Vt,
                            np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _nonparabolic_n3(phi[i], psi[i], alpha[i],
                                  E1[i], E2[i], E3[i],
                                  N1[i], N2[i], N3[i], Vt)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef void _vnonparabolic_dn3(np.ndarray[double] phi,
                             np.ndarray[double] psi,
                             np.ndarray[double] alpha,
                             np.ndarray[double] E1,
                             np.ndarray[double] E2,
                             np.ndarray[double] E3,
                             np.ndarray[double] N1,
                             np.ndarray[double] N2,
                             np.ndarray[double] N3,
                             double Vt,
                             np.ndarray[double] out):
    cdef int num = phi.shape[0]
    cdef int i
    for i in range(num):
        out[i] = _nonparabolic_dn3(phi[i], psi[i], alpha[i],
                                   E1[i], E2[i], E3[i],
                                   N1[i], N2[i], N3[i], Vt)


def boltzmann(phi, out=None):
    '''
    Boltzmann approximation to the Fermi-Dirac integral for a bulk
    semiconductor with a parabolic band.
    '''
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vboltzmann(phi, out)
        return out
    else:
        assert out is None
        return _boltzmann(phi)

def dboltzmann(phi, out=None):
    '''
    Boltzmann approximation to the first derivative of the Fermi-Dirac
    integral for a bulk semiconductor with a parabolic band.
    '''
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vdboltzmann(phi, out)
        return out
    else:
        assert out is None
        return _dboltzmann(phi)

def iboltzmann(phi, out=None):
    '''
    Boltzmann approximation to the inverse Fermi-Dirac integral for a bulk
    semiconductor with a parabolic band.
    '''
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _viboltzmann(phi, out)
        return out
    else:
        assert out is None
        return _iboltzmann(phi)

def parabolic(phi, out=None):
    '''
    Fermi-Dirac integral for a bulk semiconductor with a parabolic band.
    '''
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vparabolic(phi, out)
        return out
    else:
        assert out is None
        return _parabolic(phi)

def dparabolic(phi, out=None):
    '''
    First derivative of the Fermi-Dirac integral for a bulk semiconductor
    with a parabolic band.
    '''
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vdparabolic(phi, out)
        return out
    else:
        assert out is None
        return _dparabolic(phi)

def iparabolic(phi, out=None):
    '''
    Inverse Fermi-Dirac integral for a bulk semiconductor with a parabolic band.
    '''
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _viparabolic(phi, out)
        return out
    else:
        assert out is None
        return _iparabolic(phi)

def nonparabolic(phi, alpha, out=None):
    '''
    Fermi-Dirac integral for a bulk semiconductor with a nonparabolic band
    described by Kane's k.p model, with nonparabolicity factor `alpha`.
    '''
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(alpha, numpy.ndarray) and alpha.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vnonparabolic(phi, alpha, out)
        return out
    else:
        assert out is None
        assert not isinstance(alpha, numpy.ndarray)
        return _nonparabolic(phi, alpha)

def dnonparabolic(phi, alpha, out=None):
    '''
    First derivative of the Fermi-Dirac integral for a bulk semiconductor with
    a nonparabolic band described by Kane's k.p model, with nonparabolicity
    factor `alpha`.
    '''
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(alpha, numpy.ndarray) and alpha.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vdnonparabolic(phi, alpha, out)
        return out
    else:
        assert out is None
        assert not isinstance(alpha, numpy.ndarray)
        return _dnonparabolic(phi, alpha)

def boltzmann_p(phi, psi, E, N, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E, numpy.ndarray) and E.shape[0] == num
        assert isinstance(N, numpy.ndarray) and N.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vboltzmann_p(phi, psi, E, N, Vt, out)
        return out
    else:
        assert out is None
        return _boltzmann_p(phi, psi, E, N, Vt)

def boltzmann_n(phi, psi, E, N, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E, numpy.ndarray) and E.shape[0] == num
        assert isinstance(N, numpy.ndarray) and N.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vboltzmann_n(phi, psi, E, N, Vt, out)
        return out
    else:
        assert out is None
        return _boltzmann_n(phi, psi, E, N, Vt)

def boltzmann_dp(phi, psi, E, N, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E, numpy.ndarray) and E.shape[0] == num
        assert isinstance(N, numpy.ndarray) and N.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vboltzmann_dp(phi, psi, E, N, Vt, out)
        return out
    else:
        assert out is None
        return _boltzmann_dp(phi, psi, E, N, Vt)

def boltzmann_dn(phi, psi, E, N, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E, numpy.ndarray) and E.shape[0] == num
        assert isinstance(N, numpy.ndarray) and N.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vboltzmann_dn(phi, psi, E, N, Vt, out)
        return out
    else:
        assert out is None
        return _boltzmann_dn(phi, psi, E, N, Vt)

def iboltzmann_p(phi, psi, E, N, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E, numpy.ndarray) and E.shape[0] == num
        assert isinstance(N, numpy.ndarray) and N.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _viboltzmann_p(phi, psi, E, N, Vt, out)
        return out
    else:
        assert out is None
        return _iboltzmann_p(phi, psi, E, N, Vt)

def iboltzmann_n(phi, psi, E, N, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E, numpy.ndarray) and E.shape[0] == num
        assert isinstance(N, numpy.ndarray) and N.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _viboltzmann_n(phi, psi, E, N, Vt, out)
        return out
    else:
        assert out is None
        return _iboltzmann_n(phi, psi, E, N, Vt)


def parabolic_p(phi, psi, E, N, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E, numpy.ndarray) and E.shape[0] == num
        assert isinstance(N, numpy.ndarray) and N.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vparabolic_p(phi, psi, E, N, Vt, out)
        return out
    else:
        assert out is None
        return _parabolic_p(phi, psi, E, N, Vt)

def parabolic_n(phi, psi, E, N, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E, numpy.ndarray) and E.shape[0] == num
        assert isinstance(N, numpy.ndarray) and N.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vparabolic_n(phi, psi, E, N, Vt, out)
        return out
    else:
        assert out is None
        return _parabolic_n(phi, psi, E, N, Vt)

def parabolic_dp(phi, psi, E, N, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E, numpy.ndarray) and E.shape[0] == num
        assert isinstance(N, numpy.ndarray) and N.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vparabolic_dp(phi, psi, E, N, Vt, out)
        return out
    else:
        assert out is None
        return _parabolic_dp(phi, psi, E, N, Vt)

def parabolic_dn(phi, psi, E, N, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E, numpy.ndarray) and E.shape[0] == num
        assert isinstance(N, numpy.ndarray) and N.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vparabolic_dn(phi, psi, E, N, Vt, out)
        return out
    else:
        assert out is None
        return _parabolic_dn(phi, psi, E, N, Vt)

def iparabolic_p(phi, psi, E, N, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E, numpy.ndarray) and E.shape[0] == num
        assert isinstance(N, numpy.ndarray) and N.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _viparabolic_p(phi, psi, E, N, Vt, out)
        return out
    else:
        assert out is None
        return _iparabolic_p(phi, psi, E, N, Vt)

def iparabolic_n(phi, psi, E, N, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E, numpy.ndarray) and E.shape[0] == num
        assert isinstance(N, numpy.ndarray) and N.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _viparabolic_n(phi, psi, E, N, Vt, out)
        return out
    else:
        assert out is None
        return _iparabolic_n(phi, psi, E, N, Vt)


def nonparabolic_n(phi, psi, alpha, E, N, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(alpha, numpy.ndarray) and alpha.shape[0] == num
        assert isinstance(E, numpy.ndarray) and E.shape[0] == num
        assert isinstance(N, numpy.ndarray) and N.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vnonparabolic_n(phi, psi, alpha, E, N, Vt, out)
        return out
    else:
        assert out is None
        assert not isinstance(alpha, numpy.ndarray)
        return _nonparabolic_n(phi, psi, alpha, E, N, Vt)

def nonparabolic_dn(phi, psi, alpha, E, N, Vt, out=None):
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(alpha, numpy.ndarray) and alpha.shape[0] == num
        assert isinstance(E, numpy.ndarray) and E.shape[0] == num
        assert isinstance(N, numpy.ndarray) and N.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vnonparabolic_dn(phi, psi, alpha, E, N, Vt, out)
        return out
    else:
        assert out is None
        assert not isinstance(alpha, numpy.ndarray)
        return _nonparabolic_dn(phi, psi, alpha, E, N, Vt)



def boltzmann_n3(phi, psi, E1, E2, E3, N1, N2, N3, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E1, numpy.ndarray) and E1.shape[0] == num
        assert isinstance(E2, numpy.ndarray) and E2.shape[0] == num
        assert isinstance(E3, numpy.ndarray) and E3.shape[0] == num
        assert isinstance(N1, numpy.ndarray) and N1.shape[0] == num
        assert isinstance(N2, numpy.ndarray) and N2.shape[0] == num
        assert isinstance(N3, numpy.ndarray) and N3.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vboltzmann_n3(phi, psi,
                       E1, E2, E3,
                       N1, N2, N3, Vt, out)
        return out
    else:
        assert out is None
        return _boltzmann_n3(phi, psi,
                             E1, E2, E3,
                             N1, N2, N3, Vt)

def boltzmann_dn3(phi, psi, E1, E2, E3, N1, N2, N3, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E1, numpy.ndarray) and E1.shape[0] == num
        assert isinstance(E2, numpy.ndarray) and E2.shape[0] == num
        assert isinstance(E3, numpy.ndarray) and E3.shape[0] == num
        assert isinstance(N1, numpy.ndarray) and N1.shape[0] == num
        assert isinstance(N2, numpy.ndarray) and N2.shape[0] == num
        assert isinstance(N3, numpy.ndarray) and N3.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vboltzmann_dn3(phi, psi,
                        E1, E2, E3,
                        N1, N2, N3, Vt, out)
        return out
    else:
        assert out is None
        return _boltzmann_dn3(phi, psi,
                              E1, E2, E3,
                              N1, N2, N3, Vt)

def parabolic_n3(phi, psi, E1, E2, E3, N1, N2, N3, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E1, numpy.ndarray) and E1.shape[0] == num
        assert isinstance(E2, numpy.ndarray) and E2.shape[0] == num
        assert isinstance(E3, numpy.ndarray) and E3.shape[0] == num
        assert isinstance(N1, numpy.ndarray) and N1.shape[0] == num
        assert isinstance(N2, numpy.ndarray) and N2.shape[0] == num
        assert isinstance(N3, numpy.ndarray) and N3.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vparabolic_n3(phi, psi,
                       E1, E2, E3,
                       N1, N2, N3, Vt, out)
        return out
    else:
        assert out is None
        return _parabolic_n3(phi, psi,
                             E1, E2, E3,
                             N1, N2, N3, Vt)

def parabolic_dn3(phi, psi, E1, E2, E3, N1, N2, N3, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(E1, numpy.ndarray) and E1.shape[0] == num
        assert isinstance(E2, numpy.ndarray) and E2.shape[0] == num
        assert isinstance(E3, numpy.ndarray) and E3.shape[0] == num
        assert isinstance(N1, numpy.ndarray) and N1.shape[0] == num
        assert isinstance(N2, numpy.ndarray) and N2.shape[0] == num
        assert isinstance(N3, numpy.ndarray) and N3.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vparabolic_dn3(phi, psi,
                        E1, E2, E3,
                        N1, N2, N3, Vt, out)
        return out
    else:
        assert out is None
        return _parabolic_dn3(phi, psi,
                              E1, E2, E3,
                              N1, N2, N3, Vt)

def nonparabolic_n3(phi, psi, alpha, E1, E2, E3, N1, N2, N3, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(alpha, numpy.ndarray) and alpha.shape[0] == num
        assert isinstance(E1, numpy.ndarray) and E1.shape[0] == num
        assert isinstance(E2, numpy.ndarray) and E2.shape[0] == num
        assert isinstance(E3, numpy.ndarray) and E3.shape[0] == num
        assert isinstance(N1, numpy.ndarray) and N1.shape[0] == num
        assert isinstance(N2, numpy.ndarray) and N2.shape[0] == num
        assert isinstance(N3, numpy.ndarray) and N3.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vnonparabolic_n3(phi, psi, alpha,
                          E1, E2, E3,
                          N1, N2, N3, Vt, out)
        return out
    else:
        assert out is None
        assert not isinstance(alpha, numpy.ndarray)
        return _nonparabolic_n3(phi, psi, alpha,
                                E1, E2, E3,
                                N1, N2, N3, Vt)

def nonparabolic_dn3(phi, psi, alpha, E1, E2, E3, N1, N2, N3, Vt, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(psi, numpy.ndarray) and psi.shape[0] == num
        assert isinstance(alpha, numpy.ndarray) and alpha.shape[0] == num
        assert isinstance(E1, numpy.ndarray) and E1.shape[0] == num
        assert isinstance(E2, numpy.ndarray) and E2.shape[0] == num
        assert isinstance(E3, numpy.ndarray) and E3.shape[0] == num
        assert isinstance(N1, numpy.ndarray) and N1.shape[0] == num
        assert isinstance(N2, numpy.ndarray) and N2.shape[0] == num
        assert isinstance(N3, numpy.ndarray) and N3.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _vnonparabolic_dn3(phi, psi, alpha,
                           E1, E2, E3,
                           N1, N2, N3, Vt, out)
        return out
    else:
        assert out is None
        assert not isinstance(alpha, numpy.ndarray)
        return _nonparabolic_dn3(phi, psi, alpha,
                                 E1, E2, E3,
                                 N1, N2, N3, Vt)