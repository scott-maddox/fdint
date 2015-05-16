import os
import sys
fpath = os.path.join(os.path.dirname(__file__), '../fdint/_dgfd.pyx')
templates_dir = os.path.join(os.path.dirname(__file__), 'templates/')
gfd_Gs_path = os.path.join(templates_dir, 'gfd_Gs')
gfd_BSs_path = os.path.join(templates_dir, 'gfd_BSs')

import numpy
INF = numpy.inf

with open(fpath, 'w') as f:
    f.write('\n')
    f.write(open(gfd_Gs_path, 'r').read())
    f.write('\n')
    f.write(open(gfd_BSs_path, 'r').read())
    f.write('\n')
    
    # Generate `dgfd1h`, etc.
    for i in xrange(-1,6,2):
        k2 = str(i).replace('-','m')
        f.write('''
@cython.cdivision(True)
cdef inline double dgfd{k2}h(double phi, double beta):'''.format(k2=k2))
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
        return dgfd{k2}h{ext}(phi, beta)'''.format(k2=k2,ext=ext,phi_max=phi_max))
            else:
                f.write('''
    return dgfd{k2}h{ext}(phi, beta)
'''.format(k2=k2,ext=ext,phi_max=phi_max))
    
    
    # Generate `dgfd1h_lt_m2`, etc.
    for i in xrange(-1,6,2):
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
cdef inline double dgfd{k2}h{ext}(double phi, double beta):'''
                ''.format(k2=k2, ext=ext))
            for m, k in enumerate(xrange(i, 22, 2)):
                # m is the order of the approximation
                if m == 0:
                    continue # skip 0th order
                if m > 10:
                    break
                #TODO: binary search optimization
                if phi_max != INF:
                    f.write('''
    if(beta <= BS{k2}h{ext}__{m}):
        return dgfd{k2}h{ext}__{m}(phi, beta)'''.format(k2=k2, ext=ext, m=m))
                if m % 2 == 1:
                    last_odd_m = m
            if phi_max != INF:
                f.write('''
    warnings.warn('dgfd{k2}h: less than 24 bits of accuracy',
                  RuntimeWarning)
    # odd-order approximations (overestimation) result in better stability
    # for solid-state physics simulations
    return dgfd{k2}h{ext}__{m}(phi, beta)
'''.format(k2=k2, ext=ext, m=last_odd_m))
            else:
                f.write('''
    warnings.warn('dgfd{k2}h: 24 bits of accuracy not guaranteed',
                  RuntimeWarning)
    # odd-order approximations (overestimation) result in better stability
    # for solid-state physics simulations
    return dgfd{k2}h{ext}__{m}(phi, beta)
'''.format(k2=k2, ext=ext, m=last_odd_m))
 

    # Generate `dgfd1h_lt_m2`, etc.
    for i in xrange(-1,6,2):
        k2 = str(i).replace('-','m')
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
                if m > 10:
                    break
                f.write('''
@cython.cdivision(True)
cdef inline double dgfd{k2}h{ext}__{m}(double phi, double beta):'''
                ''.format(k2=k2, ext=ext, m=m))
                for n, _k2 in enumerate(xrange(i, 22, 2)):
                    _k2 = str(_k2).replace('-','m')
                    if n > m:
                        break
                    if n == 0:
                        f.write('''
        return (       G0 *dfd{k2}h{ext}(phi)'''.format(k2=_k2, ext=ext))
                    else:
                        mstr = str(m).replace('10','A')
                        nstr = str(n).replace('10','A')
                        f.write('''
                +beta*(G{m}{n}*dfd{k2}h{ext}(phi)'''.format(k2=_k2,
                                                                  ext=ext,
                                                                  m=mstr,
                                                                  n=nstr,
                                                                  ))
                f.write('\n                )'+')'*m+'\n')