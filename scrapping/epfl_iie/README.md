# Data collection steps

We start by _scrapping_ the various data sources to find keywords related to each lab. Scrapped data is stored in `data/scrapped`. The structure of scrapped data files is not uniform. Then, relevant data is _extracted_ and stored into `data/extracted` in `.json` files using common structures. Finally, the files are _merged_ into a smaller number of files.

Keyword groups are retrieved or computed separately.


# 🔎 Scrapping

## Cadidb

For lab names, prof name, number of accreds (includes invited and people outside EPFL).
Ask for access to `enacvm-dev`.
Run `scripts/scrap_cadidb.sql`. This gets the most up do date info.
Save table to `data/iie_labs.csv`.
Missing APHYS, APRL, ECOS (must add by hand). ECOTOX and EPFL-PSI mentioned in infoscience but missing in cadidb.

### FTE instead of unit size

Unit size can be replaced by FTE in `data/iie_labs.csv`. This info is obtained from HR. Current data from 2023.01.


## EPFL Graph

From the database. Connect to `epfl_graph` database using descriptions and credentials from the notion card. Download the tables in CSV using your favorite DBmanager.

Also contains data about labs that no longer exist.


### Research data

Run the FME workspace to process the CSV files (see `scripts/scrap_epfl_graph_research.fmw`). Data is extracted from the `Edges_N_Unit_N_Concept_T_Research` database.

The _score_ relating a keyword to a lab is a metric of __how much the lab has published on this concept__ (detected from publication's abstract).


### Teaching data

Use `scripts/scrap_epfl_graph_teaching.sql`. Data is extracted from the `Edges_N_Person_N_Concept_T_TeachingAuto` database. It is filtered by profs' SCIPERS for current labs (see `data/iie_labs.csv` for the list of profs).


## Infoscience

From `scripts`, run
```
python3 scrap_infoscience.py
```
to download all IIE entries in `xml` format in `data/scrapped/infoscience/`. Modify the number of entries to fetch if necessary. Only 1000 entries at a time can be retrieved.

We count the __number of occurrences__ of each keyword for every publication of current labs.


## Google Scholar

Done by hand. Lab's heads are searched on Google Scholar and their fields of research are added with a __score of 1__.


# 🧹 Extracting relevant data

## EPFL Graph

From `scripts`, run
```
python3 extract_info_epfl_graph.py
```
to export relevant data to `data/extracted/epfl_graph.json` and `data/extracted/epfl_graph_teaching.json`.


## Infoscience

From `scripts`, run
```
python3 extract_info_infoscience.py
```
to export relevant data to `data/extracted/infoscience.json`.


# 🌪️ Merge into single file

From `scripts`, run
```
python3 merge.py
```
This will generate `data/all_sources.json`.


# 📕 Keyword groups

## EPFL Graph

Use `scripts/scrap_epfl_graph_keywords_categories.sql` to extract _keyword -- parent category_ and _category -- parent category_ pairs, saved into `data/scrapped/epfl_graph/` in `keyword_category.csv` and `category_category.csv`.

Then, run `scripts/generate_keyword_groups_epfl_graph.py`.


## SNF Research domains and disciplines

Categories taken from [Swiss National Science Foundation](https://www.snf.ch/SiteCollectionDocuments/allg_disziplinenliste.pdf) and copied in `data/scrapped/snf/tree.txt`.

Use `scripts/classify_keywords_chatgpt.py` to generate prompts (saved in `data/prompts/snf_epfl_graph`) for classifying EPFL Graph keywords into SNF categories. Save answers in `data/keyword_groups/snf/keyword_category.json` and update `data/scrapped/snf/tree.txt` into `data/scrapped/snf/tree_augmented.txt` with categories hallucinated by ChatGPT.
