#!/usr/bin/env python

from setuptools import setup

VERSION = "0.9.0"


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
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Testing',
    ],
    keywords='tk widgets',
    install_requires=['setuptools'],
    data_files=data_files,
)
