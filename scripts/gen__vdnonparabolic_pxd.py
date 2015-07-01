import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_vdnonparabolic.pxd'))

with open(fpath, 'w') as f:
    f.write('''cpdef void vdnonparabolic(np.ndarray[double] phi, np.ndarray[double] alpha,
                          np.ndarray[double] out)
''')
