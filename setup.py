#!/usr/bin/env python

from distutils.core import setup

with open('README') as f:
    long_description = f.read()

setup(
    name='tmdb3',
    version='0.7.1',
    description='TheMovieDB.org APIv3 interface',
    long_description=long_description,
    author='Raymond Wagner',
    author_email='raymond@wagnerrp.com',
    packages=['tmdb3']
)
