from setuptools import setup
import io
import os


here = os.path.abspath(os.path.dirname(__file__))

short_description = 'Computes certain statistics incrementally'

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = short_description

setup(
    name='incremental-statistics',
    version="0.1.1",
    description=short_description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='V. Ahuir',
    author_email='viahes@upv.es',
    url="https://github.com/viahes/incremental-statistics",
    license='Apache2.0',
    packages=[
        'incremental_statistics'
    ],
)
