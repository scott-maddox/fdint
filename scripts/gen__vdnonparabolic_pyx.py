# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_vdnonparabolic.pyx'))

with open(fpath, 'w') as f:
    f.write('''
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef void vdnonparabolic(np.ndarray[double] phi, np.ndarray[double] alpha,
                          np.ndarray[double] out):
    \'\'\'
    Vectorized form of dnonparabolic.
    \'\'\'
    cdef int imax = phi.shape[0]
    assert imax == alpha.shape[0]
    assert imax == out.shape[0]
    cdef int i
    for i in range(imax):
        out[i] = dnonparabolic(phi[i], alpha[i])
''')