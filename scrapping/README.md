# Scrapping

## Cadidb

For lab names, prof name, number of accreds (includes invited and people outside EPFL).
Ask for access to enacvm-dev.
Run `scripts/scrap_cadidb.sql`. This gets the most up do date info.
Save table to `data/iie_labs.csv`.
Missing APHYS, APRL, ECOS (must add by hand). ECOTOX and EPFL-PSI mentioned in infoscience but missing in cadidb.

### FTE instead of unit size

Unit size can be replaced by FTE in `data/iie_labs.csv`. This info is obtained from HR. Current data from 2023.01.


## EPFL Graph

From the database. Also contains data about labs that no longer exist.


## Infoscience

From `scripts`, run
```
python3 scrap_infoscience.py
```
to download all IIE entries in `xml` format in `data/scrapped/infoscience/`. Modify the number of entries to fetch if necessary. Only 1000 entries at a time can be retrieved.


## Google Scholar

Done by hand.


# Extracting relevant data

## EPFL Graph

From `scripts`, run
```
python3 extract_info_epfl_graph.py
```
to export relevant data to `data/extracted/epfl_graph.json`.


## Infoscience

From `scripts`, run
```
python3 extract_info_infoscience.py
```
to export relevant data to `data/extracted/infoscience.json`.


# Merge into single file

From `scripts`, run
```
python3 merge.py
```
This will generate `data/all_sources.json`.