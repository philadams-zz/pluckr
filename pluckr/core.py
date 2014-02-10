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


def pluck(rows, fields, inverse=False):
    """
    rows: an iterable of iterables
    yield each row in `rows`, retaining only those indices of row in `fields`.
    if inverse=True, retain only those indices NOT in `fields`.
    if line_numbers=True, prepend a column 'line' starting at line=0.
    """
    retain = None
    for idx, row in enumerate(rows):

        # retain the appropriate columns
        if not inverse:
            retain = retain or fields
        else:
            retain = retain or [i for i in range(len(row)) if i not in fields]
        newrow = [row[i] for i in retain if len(row) > i]

        yield newrow


def main(args):

    # parse csv data
    rows = csv.reader(args.infile,
                      delimiter=args.delimiter, quotechar=args.quotechar)

    # if --names just display col names and exit
    if args.col_names:
        names = rows.next()
        for idx, name in enumerate(names):
            sys.stdout.write('%d. %s\n' % (idx, name))
        exit(0)

    # skip n rows
    for i in range(args.skip):
        rows.next()

    # prep fields
    if args.fields:
        fields = [int(f) for f in args.fields.replace(' ', '').split(',')]
    else:
        fields = None

    # push to stdout
    out = csv.writer(sys.stdout, lineterminator='\n')
    iter = enumerate(pluck(rows, fields, inverse=args.inverse))
    if fields is None:
        iter = enumerate(rows)
    for idx, row in iter:
        if args.line_numbers:
            row.insert(0, idx)
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
                        help='ordered list of columns to retain; zero-indexed')
    parser.add_argument('-i', '--inverse', dest='inverse', action='store_true',
                        help='invert column retention: drop those in -f')
    parser.add_argument('-d', '--delimiter', default=',', dest='delimiter',
                        help='field delimiter when reading infile')
    parser.add_argument('-q', '--quotechar', default='"', dest='quotechar',
                        help='field quotechar when reading infile')
    parser.add_argument('-s', '--skip', default=0, dest='skip',
                        type=int, help='number of rows to skip')
    parser.add_argument('-l', '--line-numbers', dest='line_numbers',
                        action='store_true',
                        help='prepend line numbers to output')
    parser.add_argument('-n', '--names', dest='col_names', action='store_true',
                        help='print column names; assumes one header row')
    args = parser.parse_args()

    main(args)
