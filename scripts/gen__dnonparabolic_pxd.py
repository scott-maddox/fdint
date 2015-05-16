import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_dnonparabolic.pxd'))

with open(fpath, 'w') as f:
    f.write('cdef double dnonparabolic(double phi, double alpha)\n')