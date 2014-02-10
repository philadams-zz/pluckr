from setuptools import setup, find_packages

version = '0.0.7'
description = 'Pluck columns from CSV files in the command line.'
description += ' Like cut or awk, but doesn\'t choke on delimiter escaping.'
with open('README.txt') as f:
    readme = f.read()

setup(
    name='pluckr',
    version=version,
    author='Phil Adams',
    author_email='philadams.net@gmail.com',
    url='https://github.com/philadams/pluckr',
    license='LICENSE.txt',
    description=description,
    long_description=readme,
    packages=find_packages(exclude=('tests', 'docs')),
    scripts=['bin/pluckr'],
)
