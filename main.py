#!/usr/bin/python
"""
Project: Address Location Tool
Repository: git@github.com:alt-locator/alt-python.git
"""
__author__ = 'Craig Nishina'
__copyright__ = 'Copyright 2017, Address Location Tool'
__license__ = 'MIT'
__maintainer__ = 'Craig Nishina'
__email__ = 'craig.nishina@gmail.com'


import sys

def main():
    """
    Command line interface for Address Location Tool.
    parameter 1 = run method
    parameter 2 = environment variable
    """

    run = None
    env = None

    if sys.argv.__len__() >= 2:
        run = sys.argv[1]
        print 'run: ' + run

    if sys.argv.__len__() >= 3:
        env = sys.argv[2]
        print 'env: ' + env

if __name__ == '__main__':
    main()
