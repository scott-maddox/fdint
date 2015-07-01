'''
Copy the ifd.pyx template to fdint/_ifd.pyx
'''

import os
import sys
templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
ifd_pyx_path = os.path.join(templates_dir, 'ifd.pyx')

fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_ifd.pyx'))
with open(fpath, 'w') as f:
    f.write(open(ifd_pyx_path, 'r').read())