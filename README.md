# CSV-Lookup
Dit script voegt een kolom toe aan een CSV met daarin opgezochte waarden uit een andere CSV.

Bijvoorbeeld: GUIDs toevoegen op basis van Bestandsnaam


## Usage:
```bash
csv-lookup.py \
	{INPUT_CSV} {INPUT_KEY_COL} \
	{LOOKUP_CSV} {LOOKUP_KEY_COL} {LOOKUP_VALUE_COL} \
	{OUTPUT_CSV}

# voorbeeld:
csv-lookup.py \
	adressen.csv "image_name" \
	Scan-GUIDs-Bestandsnaam.csv "BESCHRIJVING" "GUID" \
	adressen-met-scan-guid.csv
````