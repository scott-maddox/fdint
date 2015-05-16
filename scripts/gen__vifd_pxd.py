import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_vifd.pxd'))

with open(fpath, 'w') as f:
    for i in xrange(1,2,2):
        a = str(i).replace('-','m')
        f.write('''cpdef void vifd{a}h(np.ndarray[double] phi, np.ndarray[double] out)
'''.format(a=a))

