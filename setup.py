'''Setup file'''
from setuptools import find_packages, setup

setup(
    name='stegonosaurus',
    packages=find_packages(include=["stegonosaurus"]),
    version='1.2.0',
    description='Stegonography utilities',
    author='Geada734',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests'
)