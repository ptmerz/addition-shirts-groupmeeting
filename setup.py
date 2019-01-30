r"""
`shirts-addition` is a package aimed at demonstrating Travis CI
and readthedocs to the Shirts group at CU Boulder
"""
from setuptools import setup

#####################################
VERSION = "1.0.0rc1"
__version__ = VERSION

#####################################

setup(
    name='shirts_addition',
    version=__version__,
    description='Add numbers!',
    url='https://shirts-addition.readthedocs.io',
    author='Pascal T. Merz',
    author_email='pascal.merz@colorado.edu',
    packages=['shirts_addition']
)
