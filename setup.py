#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='schrodinger_equation',
    version='0.1.0',
    description="Schrodinger Equation solver",
    long_description=readme + '\n\n' + history,
    author="Adam Rosenstein",
    author_email='adamrosenstein19@gmail.com',
    url='https://github.com/arosenstein/schrodinger_equation',
    packages=[
        'schrodinger_equation',
    ],
    package_dir={'schrodinger_equation':
                 'schrodinger_equation'},
    entry_points={
        'console_scripts': [
            'schrodinger_equation=schrodinger_equation.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='schrodinger_equation',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
