#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup
import sys
import os
from os.path import abspath, isdir, dirname, join

VERSION = '0.1'

setup(name='popysh',
      version=VERSION,
      description='Portable Python shell',
      author='mail@agateau.com',
      packages=['popysh'],
      )
