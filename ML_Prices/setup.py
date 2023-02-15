#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Daniel Cruz",
    author_email='danielcruz.alu.lmb@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Project that sents a email, when a price of a product changes.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ML_Prices',
    name='ML_Prices',
    packages=find_packages(include=['ML_Prices', 'ML_Prices.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/DanielCruzDataEngineer/ML_Prices',
    version='1',
    zip_safe=False,
)
