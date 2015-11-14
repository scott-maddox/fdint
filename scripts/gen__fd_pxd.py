# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_fd.pxd'))

with open(fpath, 'w') as f:
    for i in xrange(-9,22,2):
        a = str(i).replace('-','m')
        f.write('cdef double fd{a}h(double phi)\n'.format(a=a))
        for b in ['lt_m2', 'm2_to_0', '0_to_2', '2_to_5', '5_to_10',
                  '10_to_20', '20_to_40', 'gt_40']:
            f.write('cdef double fd{a}h_{b}(double phi)\n'
                    ''.format(a=a,b=b))