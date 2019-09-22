#from setuptools import setup
from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='qtpi_kernel',
    version='0.1.0',
    packages=['qtpi_kernel'],
    description='Simple example of qtpi kernel python wrapper for Jupyter',
    long_description=readme,
    author='Jupyter Development Team',
    author_email='jupyter@googlegroups.com',
    url='https://github.com/miroslav14/qtpi_test_kernel.git',
    install_requires=[
        'jupyter_client', 'IPython', 'ipykernel'
    ],
   
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
)
