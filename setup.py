import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
  name='blockscore',
  version='4.1.0',
  description='Official BlockScore API library client for python',
  author='John Backus',
  author_email='john@blockscore.com',
  url='https://blockscore.com',
  license='MIT',
  install_requires=[
    'requests >= 2.1.0'
  ],
  packages=[
    'blockscore'
  ],
  package_data = {'blockscore': ['api/*', 'error/*','http_client/*']},
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ]
)

