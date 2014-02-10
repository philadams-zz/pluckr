pluckr
======

Pluck columns from csv files in the commandline. Like cut or awk, but without
choking on delimiter escaping.

install
-------

`pip install pluckr`. Done.

usage
-----

Grab columns 2 and 3 from stdin (`-f` is zero-indexed):

    pluckr -f 1,2 < sample1.csv

Or straight from a file:

    pluckr -f 2,1 sample1.csv

Your requested order is retained:

    pluckr -f 1,2 sample1.csv != pluckr -f 2,1 sample1.csv

You can also use Python's negative indices... grab the first and last cols:

    pluckr -f 0,-1 sample1.csv

Can't be sure which columns exist or what their indices are?

    pluckr --names sample1.csv

Fields that don't exist (e.g. `-f11111`) will be ignored.

Preprended line numbers can be helpful:

    cat sample1.csv | pluckr --line-numbers

Skip header row(s):

    cat sample1.csv | pluckr -s1

Grab all but the 2nd column (drop columns instead of selecting them):

    pluckr -f 1 -i < sample1.csv

Read (and write) various delimiters:

    pluckr -d, --out-delimiter=\| < with-commas.csv > with-pipes.csv

Note that passing tabs as arguments can be awkward; in a pinch, use:

    pluckr -d $'\t'

help
----

Via `--help`:

    usage: pluckr [-h] [-f FIELDS] [-i] [-d DELIMITER] [-q QUOTECHAR] [-s SKIP]
                  [-l] [-n]
                  [infile]

    Grab columns from csv input. http://github.com/philadams/pluckr

    positional arguments:
      infile                input file (.csv)

    optional arguments:
      -h, --help            show this help message and exit
      -f FIELDS, --fields FIELDS
                            ordered list of columns to retain; zero-indexed
      -i, --inverse         invert column retention: drop those in -f
      -d DELIMITER, --delimiter DELIMITER
                            field delimiter when reading infile
      -q QUOTECHAR, --quotechar QUOTECHAR
                            field quotechar when reading infile
      -s SKIP, --skip SKIP  number of rows to skip
      -l, --line-numbers    prepend line numbers to output
      -n, --names           print column names; assumes one header row

tests
-----

This project uses [roundup](https://github.com/bmizerany/roundup) for testing.
Run tests with `make test`.

future
------

- allow -f to take columns by name when there's a header row?
- implement --out-x for output delimiters etc.
- json output? or, contribute a cli to kennethreitz/tablib
- add out delimiter support
- add out quotechar support
