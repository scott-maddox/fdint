# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
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
