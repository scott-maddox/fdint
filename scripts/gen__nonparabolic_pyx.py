import os
import sys
fpath = os.path.join(os.path.dirname(__file__), '../fdint/_nonparabolic.pyx')
templates_dir = os.path.join(os.path.dirname(__file__), 'templates/')

import numpy
INF = numpy.inf

with open(fpath, 'w') as f:
    # Generate `nonparabolic`, etc.
    for i in xrange(1):
        k2 = str(i).replace('-','m')
        f.write('''
@cython.cdivision(True)
cdef inline double nonparabolic(double phi, double alpha):''')
        for phi_min, phi_max, ext in [(-INF, -2e0,    '_lt_m2'),
                                      (-2e0,  0e0,  '_m2_to_0'),
                                      ( 0e0,  2e0,   '_0_to_2'),
                                      ( 2e0,  5e0,   '_2_to_5'),
                                      ( 5e0, 10e0,  '_5_to_10'),
                                      (10e0, 20e0, '_10_to_20'),
                                      (20e0, 40e0, '_20_to_40'),
                                      (40e0,  INF,    '_gt_40')]:
            if phi_max != INF:
                #TODO: binary search optimization
                f.write('''
    if phi < {phi_max:.1f}:
        return nonparabolic{ext}(phi, 2.0*alpha)'''.format(ext=ext,phi_max=phi_max))
            else:
                f.write('''
    return nonparabolic{ext}(phi, 2.0*alpha)
'''.format(ext=ext,phi_max=phi_max))
    
    
    # Generate `nonparabolic_lt_m2`, etc.
    for i in xrange(1,2):
        k2 = str(i).replace('-','m')
        for phi_min, phi_max, ext in [(-INF, -2e0,    '_lt_m2'),
                                      (-2e0,  0e0,  '_m2_to_0'),
                                      ( 0e0,  2e0,   '_0_to_2'),
                                      ( 2e0,  5e0,   '_2_to_5'),
                                      ( 5e0, 10e0,  '_5_to_10'),
                                      (10e0, 20e0, '_10_to_20'),
                                      (20e0, 40e0, '_20_to_40'),
                                      (40e0,  INF,    '_gt_40')]:
            f.write('''
@cython.cdivision(True)
cdef inline double nonparabolic{ext}(double phi, double beta):'''
                ''.format(ext=ext))
            for m, k in enumerate(xrange(i, 22, 2)):
                # m is the order of the approximation
                if m == 0:
                    continue # skip 0th order
                if m > 9:
                    break
                #TODO: binary search optimization
                if phi_max != INF:
                    f.write('''
    if(beta <= BS1h{ext}__{m} and beta <= BS3h{ext}__{m}):
        return nonparabolic{ext}__{m}(phi, beta)'''.format(ext=ext, m=m))
                if m % 2 == 1:
                    last_odd_m = m
            if phi_max != INF:
                f.write('''
    warnings.warn('nonparabolic: less than 24 bits of accuracy',
                  RuntimeWarning)
    return nonparabolic{ext}__{m}(phi, beta)
'''.format(ext=ext, m=last_odd_m))
            else:
                f.write('''
    warnings.warn('nonparabolic: 24 bits of accuracy not guaranteed',
                  RuntimeWarning)
    return nonparabolic{ext}__{m}(phi, beta)
'''.format(ext=ext, m=last_odd_m))
 

    # Generate `nonparabolic_lt_m2`, etc.
    for phi_min, phi_max, ext in [(-INF, -2e0,    '_lt_m2'),
                                  (-2e0,  0e0,  '_m2_to_0'),
                                  ( 0e0,  2e0,   '_0_to_2'),
                                  ( 2e0,  5e0,   '_2_to_5'),
                                  ( 5e0, 10e0,  '_5_to_10'),
                                  (10e0, 20e0, '_10_to_20'),
                                  (20e0, 40e0, '_20_to_40'),
                                  (40e0,  INF,    '_gt_40')]:
        for m, _ in enumerate(xrange(i, 22, 2)):
            # m is the order of the approximation
            if m == 0:
                continue # skip 0th order
            if m > 9:
                break
            f.write('''

@cython.cdivision(True)
cdef inline double nonparabolic{ext}__{m}(double phi, double beta):
'''
                ''.format(ext=ext, m=m))
            # f1h=fd1h_lt_m2(phi), etc.
            for n, nk2 in enumerate(xrange(1, 22, 2)):
                nk2 = str(nk2).replace('-','m')
                if n > m+1:
                    break
                f.write('    cdef double f{nk2}h=fd{nk2}h{ext}(phi)\n'
                        ''.format(nk2=nk2, ext=ext))
    
            # gf1h=..., gf3h=...
            for i in xrange(1,4,2):
                k2 = str(i).replace('-','m')
                for n, nk2 in enumerate(xrange(i, 22, 2)):
                    if n > m:
                        break
                    nk2 = str(nk2).replace('-','m')
                    if n == 0:
                        f.write('    cdef double gf{k2}h=(       G0 *f{nk2}h\n'
                                ''.format(k2=k2, nk2=nk2, ext=ext))
                    else:
                        mstr = str(m).replace('10','A')
                        nstr = str(n).replace('10','A')
                        f.write('                      +beta*(G{m}{n}*f{nk2}h\n'
                                ''.format(nk2=nk2, ext=ext,
                                                               m=mstr,
                                                               n=nstr,
                                                               ))
                f.write('                      )'+')'*m+'\n')
            f.write('    return gf1h+beta*gf3h\n')