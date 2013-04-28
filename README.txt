pluckr
======

Pluck columns from csv files in the commandline. Like cut or awk, but without
choke on delimiter escaping.

install
-------

`pip install pluckr`. Done.

usage
-----

Grab columns 2 and 3 from stdin:

    pluckr -f 2,3 < sample1.csv

Or straight from a file:

    pluckr -f 2,3 sample1.csv

You can also use Python's negative indices... grab the first and last cols:

    pluckr -f 1,-1 sample1.csv

Fields that don't exist (e.g. `-f11111`) will be ignored.

Skip header row(s):

    cat sample1.csv | pluckr -s1

Read (and write) various delimiters:

    pluckr -d, --out-delimiter=\| < with-commas.csv > with-pipes.csv

Note that passing tabs as arguments can be awkward; in a pinch, use:

    pluckr -d $'\t'

help
----

Via `--help`:

    usage: pluckr [-h] [-f FIELDS] [-i INVERSE] [-d DELIMITER] [-q QUOTECHAR]
                  [-s SKIP]
                  [infile]

    Grab columns from csv input. http://github.com/philadams/pluckr

    positional arguments:
      infile                input file (.csv)

    optional arguments:
      -h, --help            show this help message and exit
      -f FIELDS, --fields FIELDS
                            the columns to grab (first column is 1)
      -i INVERSE, --inverse INVERSE
                            invert the column selection: drop them instead
      -d DELIMITER, --delimiter DELIMITER
                            field delimiter when reading infile
      -q QUOTECHAR, --quotechar QUOTECHAR
                            field quotechar when reading infile
      -s SKIP, --skip SKIP  number of rows to skip

future
------

- tests!!!
- not choke when -f not passed...
- implement -i
- implement --out-**
- allow -f to take columns by name?
- add out delimiter support
- add out quotechar support
