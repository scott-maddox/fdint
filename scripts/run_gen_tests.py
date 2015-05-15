import os
import sys
import subprocess

scripts_dir = os.path.dirname(__file__)
scripts = [
    'gen_test_fd.py',
    ]
for script in scripts:
    print 'running', script
    subprocess.call(['python', os.path.join(scripts_dir, script)])
