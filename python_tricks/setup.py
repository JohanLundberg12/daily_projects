from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("cythonloop.pyx"))  # Adjust filename if necessary
