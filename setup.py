#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest_iqa',
    packages=["pytest_iqa"],
    version='0.1.1',
    author='Dominik Lenoch, Fernando Giorgetti',
    author_email='dlenoch@redhat.com, fgiorget@redhat.com ',
    maintainer='Dominik Lenoch',
    maintainer_email='dlenoch@redhat.com',
    license='Apache Software License 2.0',
    url='https://github.com/rh-messaging-qe/iqa_common',
    description='IQA Messaging pytest integration plugin',
    long_description=read('README.md'),
    py_modules=['pytest_iqa'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=['pytest>=3.9.3'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points={
        'pytest11': [
            'pytest_iqa = pytest_iqa.plugin',
        ],
    },
)
