# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in worx_v2/__init__.py
from worx_v2 import __version__ as version

setup(
	name='worx_v2',
	version=version,
	description='Worx International',
	author='Usama Naveed',
	author_email='usamanaveed9263@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
