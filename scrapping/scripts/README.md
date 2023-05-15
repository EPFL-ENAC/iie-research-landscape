# Scrapping

## Cadidb

For lab names, prof name, number of accreds (includes invited and people outside EPFL).
Ask for access to enacvm-dev. Run `scrap_cadidb.sql`.
Save table to `iie_labs.csv`.
Missing APRL (must add by hand). ECOTOX and EPFL-PSI mentioned in infoscience but missing in cadidb.

## Infoscience

Run
```
python3 scrap_infoscience.py
```
to download all IIE entries in `xml` format in `../data/scrapped/infoscience/`. Modify the number of entries to fetch if necessary. Only 1000 entries at a time can be retrieved.


# Extracting relevant data

## Infoscience

Run
```
python3 extract_info_infoscience.py
```
to export relevant data to `../data/extracted/infoscience.json`.
