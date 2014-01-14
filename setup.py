from distutils.core import setup

version = '0.0.4'
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
    packages=['pluckr'],
    scripts=['bin/pluckr'],
)
