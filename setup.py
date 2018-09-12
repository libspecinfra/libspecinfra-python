#!/usr/bin/env python
import os

from setuptools import setup, find_packages
from setuptools.dist import Distribution

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

description = 'Python bindings for libspecinfra.'

setup_options = dict(
    name='libspecinfra-python',
    version='0.0.1',
    description=description,
    long_description=description,
    author='Masashi Terui',
    author_email='marcy9114+pypi@gmail.com',
    url='https://github.com/libspecinfra/libspecinfra-python',
    packages=find_packages(exclude=['tests*', 'specinfra*']),
    package_data={'libspecinfra': ['libspecinfra/libspecinfra.so']},
    include_package_data=True,
    distclass=BinaryDistribution,
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
    license='MIT License',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Rust',
    ],
    keywords='libspecinfra specinfra',
)

setup(**setup_options)
