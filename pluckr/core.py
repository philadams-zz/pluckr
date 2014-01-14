#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Phil Adams http://philadams.net

Grab columns from .csv files. Like cut or awk but without choking on delimiter
escaping.

See README.txt for details.
"""

import csv
import sys


def pluck(rows, fields, invert=False):
    for row in rows:
        yield [row[i] for i in fields if len(row) > i]


def main(args):

    # parse csv data
    rows = csv.reader(args.infile,
                      delimiter=args.delimiter, quotechar=args.quotechar)

    # skip n rows
    for i in range(args.skip):
        rows.next()

    # prep fields
    if args.fields:
        fields = [int(f) for f in args.fields.replace(' ', '').split(',')]
    else:
        fields = None

    # push to stdout
    out = csv.writer(sys.stdout)
    if fields is None:
        out.writerows(rows)
    else:
        for row in pluck(rows, fields):
            out.writerow(row)


def cli():
    import argparse

    # populate and parse command line options
    desc = 'Grab columns from csv input.'
    desc += '\nhttp://github.com/philadams/pluckr'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('infile', nargs='?', default=sys.stdin,
                        type=argparse.FileType('rU'), help='input file (.csv)')
    parser.add_argument('-f', '--fields', dest='fields',
                        help='the columns to grab (first column is 1)')
    parser.add_argument('-i', '--inverse', dest='inverse',
                        help='invert the column selection: drop them instead')
    parser.add_argument('-d', '--delimiter', default=',', dest='delimiter',
                        help='field delimiter when reading infile')
    parser.add_argument('-q', '--quotechar', default='"', dest='quotechar',
                        help='field quotechar when reading infile')
    parser.add_argument('-s', '--skip', default=0, dest='skip',
                        type=int, help='number of rows to skip')
    args = parser.parse_args()

    main(args)
