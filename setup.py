# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

description = """
django-pipeline compiler for eco templates
"""

setup(
    name='django-pipeline-eco',
    version='0.1.0',
    description=description,
    long_description=description,
    author='Luca Del Bianco',
    author_email='vshjxyz@gmail.com',
    url='https://github.com/vshjxyz/django-pipeline-eco',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['django-pipeline'],
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)
