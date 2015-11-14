# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_dfd.pyx'))

with open(fpath, 'w') as f:
    for i in range(-9,22,2)+range(0,21,2):
        a = str(i).replace('-','m')
        b = str(i+2).replace('-','m')
        c = (i+2)/2.
        f.write("""
@cython.cdivision(True)
cdef inline double dfd{b}h(double phi):
    '''
    First derivative of fd{b}h.
    '''
    return {c}*fd{a}h(phi)
""".format(a=a, b=b, c=repr(c)))
        
    for i in xrange(-9,22,2):
        a = str(i).replace('-','m')
        b = str(i+2).replace('-','m')
        c = (i+2)/2.
        for ext in ['lt_m2', 'm2_to_0', '0_to_2', '2_to_5', '5_to_10',
                  '10_to_20', '20_to_40', 'gt_40']:
            f.write("""
@cython.cdivision(True)
cdef inline double dfd{b}h_{ext}(double phi):
    '''
    First derivative of fd{b}h_{ext}.
    '''
    return {c}*fd{a}h_{ext}(phi)
""".format(a=a, b=b, ext=ext, c=repr(c)))