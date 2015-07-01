import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_vnonparabolic.pxd'))

with open(fpath, 'w') as f:
    f.write('''cpdef void vnonparabolic(np.ndarray[double] phi, np.ndarray[double] alpha,
                         np.ndarray[double] out)
''')
