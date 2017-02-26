#
#   Copyright (c) 2015, Scott J Maddox
#
#   This file is part of Open Band Parameters Device Simulator (OBPDS).
#
#   OBPDS is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   OBPDS is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with OBPDS.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
import sys
import os.path
from setuptools import setup, Extension
import numpy

try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except:
    if len(sys.argv) >= 1 and 'sdist' in sys.argv[1:]:
        raise RuntimeError('Cython is required to build a source distribution.')
    USE_CYTHON = False
    def no_cythonize(extensions, **_ignore):
        for extension in extensions:
            sources = []
            for sfile in extension.sources:
                path, ext = os.path.splitext(sfile)
                if ext in ('.pyx', '.py'):
                    if extension.language == 'c++':
                        ext = '.cpp'
                    else:
                        ext = '.c'
                    sfile = path + ext
                sources.append(sfile)
            extension.sources[:] = sources
        return extensions

ext = '.pyx' if USE_CYTHON else '.c'

extensions = [Extension("fdint._fdint", ["fdint/_fdint"+ext]),
              Extension("fdint.fd", ["fdint/fd"+ext]),
              Extension("fdint.dfd", ["fdint/dfd"+ext]),
              Extension("fdint.ifd", ["fdint/ifd"+ext]),
              Extension("fdint.gfd", ["fdint/gfd"+ext]),
              Extension("fdint.dgfd", ["fdint/dgfd"+ext]),
              Extension("fdint.scfd", ["fdint/scfd"+ext]),]


# read in __version__
exec(open('fdint/version.py').read())

metadata = dict(
    name='fdint',
    version=__version__,  # read from version.py
    description = 'A free, open-source python package for quickly and '
                  'precisely approximating Fermi-Dirac integrals.',
    long_description=open('README.rst').read(),
    url='http://scott-maddox.github.io/fdint',
    author='Scott J. Maddox',
    author_email='smaddox@utexas.edu',
    license='BSD',
    packages=['fdint',
              'fdint.tests',
              'fdint.examples'],
    package_dir={'fdint': 'fdint'},
    data_files=['fdint/__init__.pxd',
                'fdint/_fdint.pxd',
                'fdint/scfd.pxd',],
    test_suite='fdint.tests',
    setup_requires=['numpy'],
    install_requires=['numpy'],
#     zip_safe=True,
#     use_2to3=True,
    include_dirs=[numpy.get_include()],
    )

if USE_CYTHON:
    metadata['ext_modules'] = cythonize(extensions)
else:
    metadata['ext_modules'] = no_cythonize(extensions)

setup(**metadata)
