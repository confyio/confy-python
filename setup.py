import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='confyio',
    version='1.3.0',
    description='Official Confy API library client for python',
    author='Pavan Kumar Sunkara',
    author_email='pavan.sss1991@gmail.com',
    url='https://confy.io',
    license='BSD',
    install_requires=[
        'requests >= 2.1.0'
    ],
    packages=[
        'confy'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
