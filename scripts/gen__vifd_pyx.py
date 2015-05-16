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
