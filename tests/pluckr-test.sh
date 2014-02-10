#!/usr/bin/env roundup

describe "pluckr: like cut for csv files"

before() {
  cd ../bin
  pluckr="./pluckr"
  fixture="../fixtures/serenity-crew.csv"
  fixturetsv="../fixtures/serenity-crew.tsv"
  tmp='/tmp/tmp.csv'
  tmp2='/tmp/tmp2.csv'
}

after() {
  rm -f $tmp
  rm -f $tmp2
  cd -
}

it_shows_help_on_h() {
  $pluckr -h | head -n1 | grep 'usage'
}

it_reads_from_stdin() {
  out=$(cat $fixture | $pluckr | head -n1)
  test $out=''
}

it_reads_from_file() {
  out=$($pluckr $fixture | head -n1)
  test $out='first,last,preferred'
}

it_outputs_identity_with_no_args() {
  $pluckr $fixture > $tmp
  diff $tmp $fixture
}

it_respects_col_order_requests() {
  out=$($pluckr -f2,0,1 $fixture | head -n1)
  test $out='preferred,first,last'
}

it_understands_negative_indices() {
  out=$($pluckr -f-1,0 $fixture | head -n1)
  test $out='preferred,first'
}

it_shows_column_names() {
  $pluckr $fixture --names > $tmp
  echo "0. first\n1. last\n2. preferred" > $tmp2
  diff $tmp $tmp2
}

it_ignores_nonexistant_fields() {
  out=$($pluckr $fixture -f2,17 | head -n1)
  test $out='preferred'
}

it_skips_header_rows() {
  out=$($pluckr -s1 $fixture | head -n1)
  test $out='Malcolm,Reynolds,Mal'
}

it_handles_column_selection_inversion() {
  out=$($pluckr $fixture -f1 -i | head -n1)
  test $out='first,preferred'
}

it_parameterizes_delimiters() {
  out=$($pluckr $fixturetsv -f-1,1 -d $'\t' | head -n1)
  test $out='preferred,last'
}
