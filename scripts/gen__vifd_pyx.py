# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_vifd.pyx'))
with open(fpath, 'w') as f:
    for i in xrange(1,2,2):
        a = str(i).replace('-','m')
        f.write('''
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef void vifd{a}h(np.ndarray[double] phi, np.ndarray[double] out):
    \'\'\'
    Vectorized form of ifd{a}h.
    \'\'\'
    cdef int imax = phi.shape[0]
    assert imax == out.shape[0]
    cdef int i
    for i in range(imax):
        out[i] = ifd{a}h(phi[i])
'''.format(a=a))
