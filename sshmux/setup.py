from setuptools import setup, find_packages
import sys
import os

version = '0.1'

setup(name='sshmux',
      version=version,
      description="Work on multiple machines over ssh at once",
      long_description="""\
""",
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ssh',
      author='Padmakar Ojha',
      author_email='padmakar.ojha@gmail.com',
      url='github.com/dvopsway',
      license='GPL-3.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts': [
              'sshmux = sshmux.ssh:sshmux',
          ]
      },
      )
