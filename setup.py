#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "requests"
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='moisture_sensor',
    version='0.1.0',
    description="Detects moisture in soil. Sends an email when low moisture is detected.",
    long_description=readme + '\n\n' + history,
    author="Andy Browne",
    author_email='andy.maildrop@gmail.com',
    url='https://github.com/frankenwino/moisture_sensor',
    packages=[
        'moisture_sensor'
    ],
    package_dir={'moisture_sensor':
                 'moisture_sensor'},
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='moisture_sensor',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
