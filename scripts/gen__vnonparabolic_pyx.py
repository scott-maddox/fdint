import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_vnonparabolic.pyx'))

with open(fpath, 'w') as f:
    f.write('''
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef void vnonparabolic(np.ndarray[double] phi, np.ndarray[double] alpha,
                         np.ndarray[double] out):
    \'\'\'
    Vectorized form of nonparabolic.
    \'\'\'
    cdef int imax = phi.shape[0]
    assert imax == alpha.shape[0]
    assert imax == out.shape[0]
    cdef int i
    for i in range(imax):
        out[i] = nonparabolic(phi[i], alpha[i])
''')