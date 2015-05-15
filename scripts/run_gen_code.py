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

    'gen__fdint.py',

    'gen_fd_pyx.py',
    ]
for script in scripts:
    print 'running', script
    subprocess.call(['python', os.path.join(scripts_dir, script)])
