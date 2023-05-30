# Data collection steps

We start by _scrapping_ the various data sources to find keywords related to each lab. Scrapped data is stored in `data/scrapped`. Then, relevant data is _extracted_ and stored into `data/extracted` in `.json` files using common structures.


# 🔎 Scrapping

## Research Collection

From `scripts`, run
```
python3 scrap_research_collection.py
```
to download all IFU entries in `csv` format in `data/scrapped/research_collection/`. Modify the dates of entries to fetch if necessary (can have the format `2023-05`). Only 500 entries at a time can be retrieved.

We count the __number of occurrences__ of each keyword for every publication of current labs.


# 🧹 Extracting relevant data

## Infoscience

From `scripts`, run
```
python3 extract_info_research_collection.py
```
to export relevant data to `data/all_sources.json`.
