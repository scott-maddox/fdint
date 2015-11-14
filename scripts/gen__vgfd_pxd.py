# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_vgfd.pxd'))

with open(fpath, 'w') as f:
    for i in xrange(-1,6,2):
        a = str(i).replace('-','m')
        f.write('''cpdef void vgfd{a}h(np.ndarray[double] phi, np.ndarray[double] beta,
                    np.ndarray[double] out)
'''.format(a=a))

