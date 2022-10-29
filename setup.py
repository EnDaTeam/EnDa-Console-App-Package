from setuptools import setup, find_packages

setup(
    name='CAPP',
    version='1.0',
    author="EnDaTeam",
    packages=find_packages('CAPP'),
    package_dir={'': 'CAPP'},
    url='https://github.com/EnDaTeam/EnDa-Console-App-Package',
    keywords='console',
    install_requires=[
          'colorama>=0.4.6',
          'pystyle>=2.0',
          'pyfiglet>=0.8.0'
      ],

)