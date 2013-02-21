#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Phil Adams http://philadams.net

Grab columns from .csv files. Like cut or awk but without choking on delimiter
escaping.

See README.txt for details.
"""


def do_plucking(filenames):
    pass

def pluckr():
    pass


def cli():
    import argparse
    import sys

    # populate and parse command line options
    desc = 'Grab columns from csv input.'
    desc += '\nhttp://github.com/philadams/pluckr'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('infile', nargs='?', default=sys.stdin,
            type=argparse.FileType('r'), help='input file (.csv)')
    parser.add_argument('-f', '--fields', dest='fields',
            help='the columns to grab')
    parser.add_argument('-i', '--inverse', dest='inverse',
            help='invert the column selection: drop them instead')
    parser.add_argument('-d', '--delimiter', default=',', dest='delimiter',
            help='field delimiter when reading infile')
    parser.add_argument('-s', '--skip', default=0, dest='skip',
            help='number of rows to skip')
    args = parser.parse_args()
