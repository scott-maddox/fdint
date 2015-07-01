import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_nonparabolic.pxd'))

with open(fpath, 'w') as f:
    f.write('cdef double nonparabolic(double phi, double alpha)\n')