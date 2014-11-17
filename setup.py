#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README') as f:
    long_description = f.read()

setup(
    name='tmdb3',
    version='0.7.0',
    description='TheMovieDB.org APIv3 interface',
    long_description=long_description,
    packages=['tmdb3']
)
