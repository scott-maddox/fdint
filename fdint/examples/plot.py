# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
'''
Uses numerical integration to calculate accurate values to compare against.
'''

import os
import sys
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import fdint

import warnings
import numpy
from numpy import sqrt, exp
from scipy.integrate import quad
import matplotlib.pyplot as plt

INV_SQRT_PI_2 = 1.1283791670955126 # 2/sqrt(pi)

def quad_fdk(k, phi):
    r = quad(lambda x: (x)**(k)/(1.+exp(x-phi)),
            0, numpy.inf,epsabs=1e-300,epsrel=1e-8,limit=100)
    return r[0], r[1]

def quad_gfdk(k, phi, beta):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        def func(x):
            return (x)**(k)*sqrt(1+beta*x/2.)/(1.+exp(x-phi))
    r = quad(func, 0, numpy.inf,epsabs=1e-300,epsrel=1e-8,limit=100)
    return r[0], r[1]

def quad_nonparabolic(phi, alpha):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        def func(x):
            return sqrt(x*(1+alpha*x))*(1+2*alpha*x)/(1.+exp(x-phi))*INV_SQRT_PI_2
    r = quad(func, 0, numpy.inf,epsabs=1e-300,epsrel=1e-13,limit=100)
    return r[0], r[1]

phi = numpy.linspace(-30,100,1000)

###########
# Plot fd #
###########
def plot_fd_and_dfd():
    fig, ax1 = plt.subplots()
    prefix='fd'
    ax1.set_title(prefix)
    for k2 in xrange(-9,22,2):
        k = k2/2.
        k2s = str(k2).replace('-','m')
        
        if k2 > -3:
            quad_vals = [quad_fdk(k, x)[0] for x in phi]
            ax1.plot(phi, quad_vals, 'r--', lw=2)
          
        func = getattr(fdint,'{prefix}{k2s}h'.format(prefix=prefix,k2s=k2s))
        vals = [func(x) for x in phi]
        ax1.plot(phi, vals, 'r-')
          
        if k2 > -9:
            func = getattr(fdint,'d{prefix}{k2s}h'.format(prefix=prefix,k2s=k2s))
            vals = [func(x) for x in phi]
            ax1.plot(phi, vals, 'b-')
    ax1.set_yscale('log')

def plot_gfd_and_dgfd(beta):
    fig, ax1 = plt.subplots()
    prefix='gfd'
    ax1.set_title(prefix+' beta='+str(beta))
    for k2 in xrange(-1,6,2):
        k = k2/2.
        k2s = str(k2).replace('-','m')
        
        quad_vals = [quad_gfdk(k, x, beta)[0] for x in phi]
        ax1.plot(phi, quad_vals, 'r--', lw=2)
        
        func = getattr(fdint,'{prefix}{k2s}h'.format(prefix=prefix,k2s=k2s))
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            vals = [func(x, beta) for x in phi]
        ax1.plot(phi, vals, 'r-')
        
        func = getattr(fdint,'d{prefix}{k2s}h'.format(prefix=prefix,k2s=k2s))
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            vals = [func(x, beta) for x in phi]
        ax1.plot(phi, vals, 'b-')
    ax1.set_yscale('log')

def plot_nonparabolic_and_dnonparabolic(alpha):
    fig, ax1 = plt.subplots()
    fname='nonparabolic'
    ax1.set_title(fname+' alpha='+str(alpha))
    
    quad_vals = [quad_nonparabolic(x, alpha)[0] for x in phi]
    ax1.plot(phi, quad_vals, 'r--', lw=2)
    
    func = getattr(fdint,'{fname}'.format(fname=fname))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        vals = [func(x, alpha) for x in phi]
    ax1.plot(phi, vals, 'r-')
    
    func = getattr(fdint,'d{fname}'.format(fname=fname))
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        vals = [func(x, alpha) for x in phi]
    ax1.plot(phi, vals, 'b-')

    ax1.set_yscale('log')

plot_fd_and_dfd() # parabolic
plot_gfd_and_dgfd(beta=0.0) # parabolic
plot_gfd_and_dgfd(beta=0.14) # InAs
plot_gfd_and_dgfd(beta=0.3) # InSb
plot_nonparabolic_and_dnonparabolic(alpha=0.07) # InAs
plot_nonparabolic_and_dnonparabolic(alpha=0.15) # InSb
plt.show()