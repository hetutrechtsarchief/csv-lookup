#!/usr/bin/env python3

# this script adds a column to a csv with values matches values from another csv

import csv,sys,os
from sys import argv

delimiter=";"
encoding="utf-8"

if len(argv)!=7:
  sys.exit("Usage: "+os.path.basename(argv[0])+" {INPUT_CSV} {INPUT_KEY_COL} {LOOKUP_CSV} {LOOKUP_KEY_COL} {LOOKUP_VALUE_COL} {OUTPUT_CSV}")

_,INPUT_CSV,INPUT_KEY_COL,LOOKUP_CSV,LOOKUP_KEY_COL,LOOKUP_VALUE_COL,OUTPUT_CSV = argv

lut = { row[LOOKUP_KEY_COL]:row for row in csv.DictReader(open(LOOKUP_CSV, encoding=encoding)) }

reader = csv.DictReader(open(INPUT_CSV, encoding=encoding), delimiter=delimiter)

writer = csv.DictWriter(open(OUTPUT_CSV, "w", encoding=encoding), fieldnames=reader.fieldnames, delimiter=delimiter)
writer.fieldnames.append(LOOKUP_VALUE_COL)
writer.writeheader()

for r in reader:
  input_value = r[INPUT_KEY_COL] # + ".jpg" # .jpg toevoegen hier was tijdelijk om te voorkomen dat ik extensies moet weghalen uit de csv
  output_value = lut[input_value][LOOKUP_VALUE_COL]
  r[LOOKUP_VALUE_COL] = output_value 
  writer.writerow(r)
