# setup.py
from setuptools import setup, Extension

module = Extension('module', sources=['src/module.c'])

setup(
    name='python_to_cpython',
    version='1.0',
    description='Convert Python code to CPython for better performance',
    ext_modules=[module]
)
