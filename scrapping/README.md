# Scrapping

## Cadidb

For lab names, prof name, number of accreds (includes invited and people outside EPFL).
Ask for access to enacvm-dev. Run `scripts/scrap_cadidb.sql`.
Save table to `scripts/iie_labs.csv`.
Missing APRL (must add by hand). ECOTOX and EPFL-PSI mentioned in infoscience but missing in cadidb.

## Infoscience

From `scripts`, run
```
python3 scrap_infoscience.py
```
to download all IIE entries in `xml` format in `data/scrapped/infoscience/`. Modify the number of entries to fetch if necessary. Only 1000 entries at a time can be retrieved.

## Google Scholar

Done by hand.


# Extracting relevant data

## Infoscience

From `scripts`, run
```
python3 extract_info_infoscience.py
```
to export relevant data to `data/extracted/infoscience.json`.
