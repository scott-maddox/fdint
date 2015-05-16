import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_vdfd.pxd'))

with open(fpath, 'w') as f:
    for i in range(-7,24,2)+range(2,23,2):
        a = str(i).replace('-','m')
        f.write('''cpdef void vdfd{a}h(np.ndarray[double] phi, np.ndarray[double] out)
'''.format(a=a))


