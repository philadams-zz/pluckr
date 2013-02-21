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

Skip header row(s):

    cat sample1.csv | pluckr -s1

Read (and write) various delimiters:

    pluckr -d, --out-delimiter=| < with-commas.csv > with-pipes.csv

help
----

Via `--help`:

    usage: pluckr [-h] [-f FIELDS] [-i INVERSE] [-d DELIMITER] [-s SKIP] [infile]

    Grab columns from csv input. http://github.com/philadams/pluckr

    positional arguments:
      infile                input file (.csv)

    optional arguments:
      -h, --help            show this help message and exit
      -f FIELDS, --fields FIELDS
                            the columns to grab
      -i INVERSE, --inverse INVERSE
                            invert the column selection: drop them instead
      -d DELIMITER, --delimiter DELIMITER
                            field delimiter when reading infile
      -s SKIP, --skip SKIP  number of rows to skip

future
------

- add out delimiter support
- add out quotechar support
