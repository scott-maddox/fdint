import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_fd_whole.pxd'))

with open(fpath, 'w') as f:
    for i in xrange(0,21,2):
        a = str(i).replace('-','m')
        f.write('cdef double fd{a}h(double phi)\n'.format(a=a))