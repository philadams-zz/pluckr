
from distutils.core import setup

with open('README.txt') as f:
    readme = f.read()

setup(
    name='pluckr',
    version='0.0.1',
    author='Phil Adams',
    author_email='phil@philadams.net',
    url='https://github.com/philadams/pluckr',
    license='LICENSE.txt',
    description='Pluck columns from CSV files in the command line. Like cut or awk, but doesn\'t choke on delimiter escaping.',
    long_description=readme,
    packages=['pluckr'],
    scripts=['bin/pluckr'],
)

