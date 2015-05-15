import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_vfd.pxd'))

with open(fpath, 'w') as f:
    for i in xrange(-9,22,2):
        a = str(i).replace('-','m')
        f.write('''cpdef void vfd{a}h(np.ndarray[double] phi, np.ndarray[double] out)
'''.format(a=a))

    for i in xrange(0,21,2):
        a = str(i).replace('-','m')
        f.write('''cpdef void vfd{a}h(np.ndarray[double] phi, np.ndarray[double] out)
'''.format(a=a))
