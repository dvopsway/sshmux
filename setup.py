from setuptools import setup, find_packages

version = '0.1.4'

setup(name='sshmux',
      version=version,
      description="Work on multiple machines over ssh at once",
      long_description="""\
""",
      classifiers=[],
      keywords='ssh',
      author='Padmakar Ojha',
      author_email='padmakar.ojha@gmail.com',
	  url='https://github.com/dvopsway/sshmux',
      license='GPL-3.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=["pexpect","click"],
      entry_points={
          'console_scripts': [
              'sshmux = sshmux.ssh:sshmux',
          ]
      },
      )
