# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
'''
Runs all of the code-generating scripts in the correct sequence.
'''
import os
import sys
import subprocess

scripts_dir = os.path.dirname(__file__)
scripts = [
    'gen__fd_pxd.py',
    'gen__fd_pyx.py',
    'gen__fd_whole_pxd.py',
    'gen__fd_whole_pyx.py',
    'gen__vfd_pxd.py',
    'gen__vfd_pyx.py',

    'gen__dfd_pxd.py',
    'gen__dfd_pyx.py',
    'gen__vdfd_pxd.py',
    'gen__vdfd_pyx.py',

    'gen__ifd_pxd.py',
    'gen__ifd_pyx.py',
    'gen__vifd_pxd.py',
    'gen__vifd_pyx.py',

    'gen__gfd_pxd.py',
    'gen__gfd_pyx.py',
    'gen__vgfd_pxd.py',
    'gen__vgfd_pyx.py',

    'gen__dgfd_pxd.py',
    'gen__dgfd_pyx.py',
    'gen__vdgfd_pxd.py',
    'gen__vdgfd_pyx.py',

    'gen__nonparabolic_pxd.py',
    'gen__nonparabolic_pyx.py',
    'gen__vnonparabolic_pxd.py',
    'gen__vnonparabolic_pyx.py',

    'gen__dnonparabolic_pxd.py',
    'gen__dnonparabolic_pyx.py',
    'gen__vdnonparabolic_pxd.py',
    'gen__vdnonparabolic_pyx.py',

    'gen__fdint.py',

    'gen_fd_pyx.py',
    'gen_dfd_pyx.py',
    'gen_ifd_pyx.py',
    'gen_gfd_pyx.py',
    'gen_dgfd_pyx.py',
    ]
for script in scripts:
    print 'running', script
    subprocess.call(['python', os.path.join(scripts_dir, script)])
