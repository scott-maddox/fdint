# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_dfd.pxd'))

with open(fpath, 'w') as f:
    for i in range(-9,22,2)+range(0,21,2):
        k2a = str(i).replace('-','m')
        k2b = str(i+2).replace('-','m')
        f.write('cdef double dfd{k2}h(double phi)\n'.format(k2=k2b))

    for i in xrange(-9,22,2):
        k2a = str(i).replace('-','m')
        k2b = str(i+2).replace('-','m')
        for ext in ['lt_m2', 'm2_to_0', '0_to_2', '2_to_5', '5_to_10',
                  '10_to_20', '20_to_40', 'gt_40']:
            f.write('cdef double dfd{k2}h_{ext}(double phi)\n'
                    ''.format(k2=k2b,ext=ext))