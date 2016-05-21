#!/usr/bin/env python

from setuptools import setup

VERSION = "0.9.2"


with open('README.rst') as f:
    LONG_DESCR = f.read()

data_files = []

setup(
    name='belfrywidgets',
    version=VERSION,
    description='A collection of useful tkinter widgets.',
    long_description=LONG_DESCR,
    author='Revar Desmera',
    author_email='revarbat@gmail.com',
    url='https://github.com/revarbat/belfrywidgets',
    download_url='https://github.com/revarbat/belfrywidgets/archive/master.zip',
    packages=['belfrywidgets'],
    license='BSD 2-clause',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: MacOS X',
        'Environment :: MacOS X :: Aqua',
        'Environment :: MacOS X :: Carbon',
        'Environment :: MacOS X :: Cocoa',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
    ],
    keywords='tkinter widgets',
    install_requires=['setuptools'],
    data_files=data_files,
)
