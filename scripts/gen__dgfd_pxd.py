# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_dgfd.pxd'))

with open(fpath, 'w') as f:
    for i in xrange(-1,6,2):
        k2 = str(i).replace('-','m')
        f.write('cdef double dgfd{k2}h(double phi, double beta)\n'.format(k2=k2))

    for i in xrange(-1,6,2):
        k2 = str(i).replace('-','m')
        for ext in ['lt_m2', 'm2_to_0', '0_to_2', '2_to_5', '5_to_10',
                  '10_to_20', '20_to_40', 'gt_40']:
            f.write('cdef double dgfd{k2}h_{ext}(double phi, double beta)\n'
                    ''.format(k2=k2,ext=ext))

    for i in xrange(-1,6,2):
        k2 = str(i).replace('-','m')
        for ext in ['lt_m2', 'm2_to_0', '0_to_2', '2_to_5', '5_to_10',
                  '10_to_20', '20_to_40', 'gt_40']:
            for m, _ in enumerate(xrange(i, 22, 2)):
                # m is the order of the approximation
                if m == 0:
                    continue # skip 0th order
                if m > 10:
                    break
                f.write('cdef double dgfd{k2}h_{ext}__{m}(double phi, double beta)\n'
                        ''.format(k2=k2, ext=ext, m=m))