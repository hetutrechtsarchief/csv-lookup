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
  input_value = r[INPUT_KEY_COL] + ".jpg" # .jpg is tijdelijk om te voorkomen dat ik extensies moet weghalen uit de csv
  
  # if input_value in lut:
  output_value = lut[input_value][LOOKUP_VALUE_COL]
  # print(output_value)
  r[LOOKUP_VALUE_COL] = output_value 
  writer.writerow(r)





#   print(r["BESCHRIJVING"])


# image_name=BESCHRIJVING


# split_field_name = argv[1]
# input_filename = argv[2]
# output_folder = argv[3] 
# output_writers = {}

# with open(input_filename, 'rt', encoding=encoding) as input_file:
#   reader = csv.reader(input_file, delimiter=delimiter)
#   header = next(reader)

#   for r in csv.DictReader(input_file, fieldnames=header, delimiter=delimiter):

#     split_field_value = dict(r)[split_field_name]

#     if split_field_value not in output_writers:
#       output_filepath = output_folder + "/" + os.path.basename(input_filename).replace(".csv",f"-{split_field_value}.csv")
#       output_writers[split_field_value] = csv.DictWriter(open(output_filepath,"w"), fieldnames=header, delimiter=delimiter)
#       output_writers[split_field_value].writeheader()

#     output_writers[split_field_value].writerow(r)
