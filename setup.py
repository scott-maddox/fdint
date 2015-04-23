import os
import sys

# BEFORE importing distutils, remove MANIFEST. distutils doesn't properly
# update it when the contents of directories change.
if os.path.exists('MANIFEST'): os.remove('MANIFEST')


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)

    config.add_subpackage('fdint')
    config.get_version('fdint/version.py') # sets config.version
    return config


def setup_package():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)

    metadata = dict(
        name = 'fdint',
        author='Scott J. Maddox',
        author_email='smaddox@utexas.edu',
        description = 'A free, open-source python package for computing '
                      'Fermi-Dirac integrals.',
        long_description = open('README.rst').read(),
        url='http://scott-maddox.github.io/fdint',
        license='AGPLv3',
        test_suite='nose.collector',
    )

    # Run build
    if len(sys.argv) >= 2 and ('--help' in sys.argv[1:] or
            sys.argv[1] in ('--help-commands', 'egg_info', '--version',
                            'clean')):
        # Use setuptools for these commands (they don't work well or at all
        # with distutils).  For normal builds use distutils.
        try:
            from setuptools import setup
        except ImportError:
            from distutils.core import setup
    else:
        if len(sys.argv) >= 2 and sys.argv[1] == 'bdist_wheel':
            # bdist_wheel needs setuptools
            import setuptools
        from numpy.distutils.core import setup
        metadata['configuration'] = configuration

    try:
        setup(**metadata)
    finally:
        del sys.path[0]
        os.chdir(old_path)
    return


if __name__ == '__main__':
    setup_package()