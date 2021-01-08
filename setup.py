from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Sales cannibalization search using dunnhumby open data (https://www.dunnhumby.com/source-files/). Task includes several steps - data preparation, cannibalization calculation, price/discount optimization using cannibalization. ',
    author='Dmitry Bodunov',
    license='MIT',
)
