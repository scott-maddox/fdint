# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
'''
Runs all of the test-code-generating scripts in the correct sequence.

This should only be run after running ``run_gen_code.py`` and
after building with ``python setup.py build_ext --inplace``.
'''
import os
import sys
import subprocess

scripts_dir = os.path.dirname(__file__)
scripts = [
    'gen_test_fd.py',
    'gen_test_ifd.py',
    'gen_test_gfd.py',
    'gen_test_scfd.py',
    ]
for script in scripts:
    print 'running', script
    subprocess.call(['python', os.path.join(scripts_dir, script)])
