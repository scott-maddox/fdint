import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_vdgfd.pyx'))

with open(fpath, 'w') as f:
    for i in xrange(-1,6,2):
        a = str(i).replace('-','m')
        f.write('''
@cython.boundscheck(False)
@cython.wraparound(False)
cpdef void vdgfd{a}h(np.ndarray[double] phi, np.ndarray[double] beta,
                    np.ndarray[double] out):
    \'\'\'
    Vectorized form of dgfd{a}h.
    \'\'\'
    cdef int imax = phi.shape[0]
    assert imax == beta.shape[0]
    assert imax == out.shape[0]
    cdef int i
    for i in range(imax):
        out[i] = dgfd{a}h(phi[i], beta[i])
'''.format(a=a))
