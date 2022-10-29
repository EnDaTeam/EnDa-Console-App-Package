from setuptools import setup, find_packages

setup(
    name='CAPP',
    version='1',
    author="EnDaTeam",
    packages=find_packages('CAPP'),
    package_dir={'': 'CAPP'},
    url='https://github.com/EnDaTeam/EnDa-Console-App-Package',
    keywords='console',
    install_requires=[
          'os',
          'colorama',
          'pystyle',
          'sys',
          'time',
          'pyfiglet'
      ],

)