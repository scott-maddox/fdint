'''
Uses numerical integration to calculate accurate values for gfd, and then
determines the beta's at which to transition between polynomial orders of
approximation.

This only really needed to be run once, but it's here in case changes are
made that require rerunning it.

In order to run this, the branchless generalized Fermi-Dirac fuctions
(e.g. `gfd1h_lt_m2__1`, etc.) should be copied from from `_fdint.pyx`
into `_gfd_branchless.pyx`, and changed from `cdef` to `def`. Also,
`from . import _gfd_branchless` should be added to `fdint/__init__.py`.
'''

import os
import sys
fpath = os.path.join(os.path.dirname(__file__), 'gfd_BSs')

# import the local fdint
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import fdint
tests_dir = os.path.join(os.path.dirname(__file__), '../../fdint/tests/')

import numpy
from numpy import sqrt, exp
INF = numpy.inf
from scipy.integrate import quad
from scipy.optimize import brentq

def quad_gfdk(k, phi, beta):
    def func(x):
        return (x)**(k)*sqrt(1+beta*x/2.)/(1.+exp(x-phi))
    r = quad(func, 0, numpy.inf,epsabs=1e-300,epsrel=1e-13,limit=100)
    return r[0], r[1]

def find_threshold_beta(f, k, phi):
    eps = 1.19e-07
    def func(beta):
        estimate = f(phi, beta)
        ground_truth, _ground_truth_aerr = quad_gfdk(k, phi, beta)
        rerr = abs(estimate-ground_truth)/ground_truth
        return rerr - eps
    return brentq(func, 0., 1000.)
        

with open(fpath, 'w') as fout:
    for i in xrange(-1,6,2):
        k = i/2.
        k2 = str(i).replace('-','m')
        for phi_min, phi_max, ext in [(-INF, -2e0,    '_lt_m2'),
                                      (-2e0,  0e0,  '_m2_to_0'),
                                      ( 0e0,  2e0,   '_0_to_2'),
                                      ( 2e0,  5e0,   '_2_to_5'),
                                      ( 5e0, 10e0,  '_5_to_10'),
                                      (10e0, 20e0, '_10_to_20'),
                                      (20e0, 40e0, '_20_to_40'),
                                      (40e0,  INF,    '_gt_40')]:
            if phi_max == INF:
                break
            for m, _ in enumerate(xrange(i, 22, 2)):
                # m is the order of the approximation
                if m == 0:
                    continue # skip 0th order
                if m > 10:
                    break
                fname = 'gfd{k2}h{ext}__{m}'.format(k2=k2, ext=ext, m=m)
                BSname = 'BS{k2}h{ext}__{m}'.format(k2=k2, ext=ext, m=m)
                f = getattr(fdint._gfd_branchless, fname)
                threshold = find_threshold_beta(f, k, phi_max)
                fout.write('DEF {} = {:.8e}\n'.format(BSname, threshold))