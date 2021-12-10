#  -*- coding: utf-8


from distutils.core import setup


import sys


if __name__ == "__main__":
    if sys.version_info[:2] < (3, 6):
        print('Requires Python version 3.6 or later')
        sys.exit(-1)
          
    setup(name='musica_dcc_ufmg',
          packages=['μsica'],
          version='0.01',
          description='μsica utilities for the MIR course at UFMG',
          author='Flavio Figueiredo')
