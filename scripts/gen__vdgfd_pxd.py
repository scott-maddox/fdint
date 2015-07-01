import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_vdgfd.pxd'))

with open(fpath, 'w') as f:
    for i in xrange(-1,6,2):
        a = str(i).replace('-','m')
        f.write('''cpdef void vdgfd{a}h(np.ndarray[double] phi, np.ndarray[double] beta,
                    np.ndarray[double] out)
'''.format(a=a))

