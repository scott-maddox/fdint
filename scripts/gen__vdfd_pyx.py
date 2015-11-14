# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_vdfd.pyx'))

with open(fpath, 'w') as f:
    for i in range(-7,24,2)+range(2,23,2):
        a = str(i).replace('-','m')
        f.write('''
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef void vdfd{a}h(np.ndarray[double] phi, np.ndarray[double] out):
    \'\'\'
    Vectorized form of dfd{a}h.
    \'\'\'
    cdef int imax = phi.shape[0]
    assert imax == out.shape[0]
    cdef int i
    for i in range(imax):
        out[i] = dfd{a}h(phi[i])
'''.format(a=a))

