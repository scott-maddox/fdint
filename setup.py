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
from setuptools import setup
from Cython.Build import cythonize
import numpy

# read in __version__
exec(open('fdint/version.py').read())

setup(
      name='fdint',
      version=__version__,  # read from version.py
      description = 'A free, open-source python package for computing '
                    'Fermi-Dirac integrals.',
      long_description=open('README.rst').read(),
      url='http://scott-maddox.github.io/fdint',
      author='Scott J. Maddox',
      author_email='smaddox@utexas.edu',
      license='AGPLv3',
      packages=['fdint',
                'fdint.tests',
                'fdint.examples'],
      package_dir={'fdint': 'fdint'},
      test_suite='fdint.tests',
      setup_requires=['cython',
                      'numpy'],
      install_requires=['numpy'],
      zip_safe=True,
      use_2to3=True,
      # Cython
      ext_modules=cythonize('fdint/*.pyx'),
      include_dirs=[numpy.get_include()],
      )