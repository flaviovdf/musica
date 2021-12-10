#  -*- coding: utf-8


import sys


if __name__ == "__main__":
    if sys.version_info[:2] < (3, 9):
        print('Requires Python version 3.9 or later')
        sys.exit(-1)
          
    setup(name='μsica',
          py_modules=['μsica'],
          version='0.01',
          description='μsica utilities for the MIR course at UFMG',
          author='Flavio Figueiredo')
