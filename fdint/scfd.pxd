# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
cimport numpy as np
cdef double _boltzmann(double phi)
cdef double _dboltzmann(double phi)
cdef double _iboltzmann(double nu)
cdef double _parabolic(double phi)
cdef double _dparabolic(double phi)
cdef double _iparabolic(double nu)
cdef double _nonparabolic(double phi, double alpha)
cdef double _dnonparabolic(double phi, double alpha)
cdef double _boltzmann_p(double phi, double psi, double E, double N,
                         double Vt)
cdef double _boltzmann_n(double phi, double psi, double E, double N,
                         double Vt)
cdef double _boltzmann_dp(double phi, double psi, double E, double N,
                          double Vt)
cdef double _boltzmann_dn(double phi, double psi, double E, double N,
                          double Vt)
cdef double _iboltzmann_p(double n, double psi, double E, double N,
                          double Vt)
cdef double _iboltzmann_n(double n, double psi, double E, double N,
                          double Vt)
cdef double _parabolic_p(double phi, double psi, double E, double N,
                         double Vt)
cdef double _parabolic_n(double phi, double psi, double E, double N,
                         double Vt)
cdef double _parabolic_dp(double phi, double psi, double E, double N,
                          double Vt)
cdef double _parabolic_dn(double phi, double psi, double E, double N,
                          double Vt)
cdef double _iparabolic_p(double n, double psi, double E, double N,
                          double Vt)
cdef double _iparabolic_n(double n, double psi, double E, double N,
                          double Vt)
cdef double _nonparabolic_n(double phi, double psi, double alpha,
                            double E, double N, double Vt)
cdef double _nonparabolic_dn(double phi, double psi, double alpha,
                             double E, double N, double Vt)
cdef double _boltzmann_n3(double phi, double psi,
                             double E1, double E2, double E3,
                             double N1, double N2, double N3,
                             double Vt)
cdef double _boltzmann_dn3(double phi, double psi,
                              double E1, double E2, double E3,
                              double N1, double N2, double N3,
                              double Vt)
cdef double _parabolic_n3(double phi, double psi,
                             double E1, double E2, double E3,
                             double N1, double N2, double N3,
                             double Vt)
cdef double _parabolic_dn3(double phi, double psi,
                              double E1, double E2, double E3,
                              double N1, double N2, double N3,
                              double Vt)
cdef double _nonparabolic_n3(double phi, double psi, double alpha,
                             double E1, double E2, double E3,
                             double N1, double N2, double N3,
                             double Vt)
cdef double _nonparabolic_dn3(double phi, double psi, double alpha,
                              double E1, double E2, double E3,
                              double N1, double N2, double N3,
                              double Vt)
cdef void _vboltzmann(np.ndarray[double] phi,
                      np.ndarray[double] out)
cdef void _vdboltzmann(np.ndarray[double] phi,
                       np.ndarray[double] out)
cdef void _viboltzmann(np.ndarray[double] phi,
                       np.ndarray[double] out)
cdef void _vparabolic(np.ndarray[double] phi,
                      np.ndarray[double] out)
cdef void _vdparabolic(np.ndarray[double] phi,
                       np.ndarray[double] out)
cdef void _viparabolic(np.ndarray[double] phi,
                       np.ndarray[double] out)
cdef void _vnonparabolic(np.ndarray[double] phi,
                         np.ndarray[double] alpha,
                         np.ndarray[double] out)
cdef void _vdnonparabolic(np.ndarray[double] phi,
                          np.ndarray[double] alpha,
                          np.ndarray[double] out)
cdef void _vboltzmann_p(np.ndarray[double] phi,
                        np.ndarray[double] psi,
                        np.ndarray[double] E,
                        np.ndarray[double] N,
                        double Vt,
                        np.ndarray[double] out)
cdef void _vboltzmann_n(np.ndarray[double] phi,
                        np.ndarray[double] psi,
                        np.ndarray[double] E,
                        np.ndarray[double] N,
                        double Vt,
                        np.ndarray[double] out)
cdef void _vboltzmann_dp(np.ndarray[double] phi,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                        double Vt,
                        np.ndarray[double] out)
cdef void _vboltzmann_dn(np.ndarray[double] phi,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                         double Vt,
                         np.ndarray[double] out)
cdef void _viboltzmann_p(np.ndarray[double] n,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                         double Vt,
                         np.ndarray[double] out)
cdef void _viboltzmann_n(np.ndarray[double] n,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                         double Vt,
                         np.ndarray[double] out)
cdef void _vparabolic_p(np.ndarray[double] phi,
                        np.ndarray[double] psi,
                        np.ndarray[double] E,
                        np.ndarray[double] N,
                        double Vt,
                        np.ndarray[double] out)
cdef void _vparabolic_n(np.ndarray[double] phi,
                        np.ndarray[double] psi,
                        np.ndarray[double] E,
                        np.ndarray[double] N,
                        double Vt,
                        np.ndarray[double] out)
cdef void _vparabolic_dp(np.ndarray[double] phi,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                         double Vt,
                         np.ndarray[double] out)
cdef void _vparabolic_dn(np.ndarray[double] phi,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                         double Vt,
                         np.ndarray[double] out)
cdef void _viparabolic_p(np.ndarray[double] n,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                         double Vt,
                         np.ndarray[double] out)
cdef void _viparabolic_n(np.ndarray[double] n,
                         np.ndarray[double] psi,
                         np.ndarray[double] E,
                         np.ndarray[double] N,
                         double Vt,
                         np.ndarray[double] out)
cdef void _vnonparabolic_n(np.ndarray[double] phi,
                           np.ndarray[double] psi,
                           np.ndarray[double] alpha,
                           np.ndarray[double] E,
                           np.ndarray[double] N,
                           double Vt,
                           np.ndarray[double] out)
cdef void _vnonparabolic_dn(np.ndarray[double] phi,
                            np.ndarray[double] psi,
                            np.ndarray[double] alpha,
                            np.ndarray[double] E,
                            np.ndarray[double] N,
                            double Vt,
                            np.ndarray[double] out)
cdef void _vboltzmann_n3(np.ndarray[double] phi,
                         np.ndarray[double] psi,
                         np.ndarray[double] E1,
                         np.ndarray[double] E2,
                         np.ndarray[double] E3,
                         np.ndarray[double] N1,
                         np.ndarray[double] N2,
                         np.ndarray[double] N3,
                         double Vt,
                         np.ndarray[double] out)
cdef void _vboltzmann_dn3(np.ndarray[double] phi,
                          np.ndarray[double] psi,
                          np.ndarray[double] E1,
                          np.ndarray[double] E2,
                          np.ndarray[double] E3,
                          np.ndarray[double] N1,
                          np.ndarray[double] N2,
                          np.ndarray[double] N3,
                          double Vt,
                          np.ndarray[double] out)
cdef void _vparabolic_n3(np.ndarray[double] phi,
                         np.ndarray[double] psi,
                         np.ndarray[double] E1,
                         np.ndarray[double] E2,
                         np.ndarray[double] E3,
                         np.ndarray[double] N1,
                         np.ndarray[double] N2,
                         np.ndarray[double] N3,
                         double Vt,
                         np.ndarray[double] out)
cdef void _vparabolic_dn3(np.ndarray[double] phi,
                          np.ndarray[double] psi,
                          np.ndarray[double] E1,
                          np.ndarray[double] E2,
                          np.ndarray[double] E3,
                          np.ndarray[double] N1,
                          np.ndarray[double] N2,
                          np.ndarray[double] N3,
                          double Vt,
                          np.ndarray[double] out)
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
                            np.ndarray[double] out)
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
                             np.ndarray[double] out)