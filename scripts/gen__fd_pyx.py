import os
import sys
fpath = os.path.join(os.path.dirname(__file__), '../fdint/_fd.pyx')
templates_dir = os.path.join(os.path.dirname(__file__), 'templates/')
fd_branchless_pyx_path = os.path.join(templates_dir, 'fd_branchless.pyx')

with open(fpath, 'w') as f:
    for i in xrange(-9,22,2):
        k2 = str(i).replace('-','m')
        f.write('''
@cython.cdivision(True)
cdef inline double fd{k2}h(double phi):
    if phi < -2e0:
        return fd{k2}h_lt_m2(phi)
    if phi < 0e0:
        return fd{k2}h_m2_to_0(phi)
    if phi < 2e0:
        return fd{k2}h_0_to_2(phi)
    if phi < 5e0:
        return fd{k2}h_2_to_5(phi)
    if phi < 10e0:
        return fd{k2}h_5_to_10(phi)
    if phi < 20e0:
        return fd{k2}h_10_to_20(phi)
    if phi < 40e0:
        return fd{k2}h_20_to_40(phi)
    return fd{k2}h_gt_40(phi)
'''.format(k2=k2))
    f.write('\n')
    f.write(open(fd_branchless_pyx_path, 'r').read())
