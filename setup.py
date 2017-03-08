import setuptools
from setuptools.command.test import test as TestCommand
import subprocess
import pytest
import sys


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name = 'AltPy',
    version = '0.0.1',
    description='Address Location Tool in Python',
    long_description = readme,
    author = 'Craig Nishina',
    author_email = 'craig.nishina@gmail.com',
    url = 'https://github.com/alt-locator/alt-python',
    license = license,
    packages = setuptools.find_packages(exclude=('tests', 'docs')),
    cmdclass = {
        'test': PyTest,
    },
    entry_points = {
        'console_scripts': ['yapf = yapf:run_main'],
    })
