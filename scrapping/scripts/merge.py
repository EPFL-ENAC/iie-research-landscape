import csv
import json
import os


input_files = [
    "../data/extracted/epfl_graph.json",
    "../data/extracted/infoscience.json",
    "../data/scrapped/google_scholar.json",
]
sources = ["epfl_graph", "infoscience", "google_scholar"]
output_dir = "../data"
output_filename = "all_sources.json"


# Saved data
# {
#     "lab_name": {
#         "size": float,
#         "keywords_infoscience": {
#             "keyword": int,
#             ...
#         },
#         "keywords_google_scholar": {
#             "keyword": int,
#             ...
#         },
#     },
#     ...
# }
data = {}


# Load list of labs for filtering
# get lab name from first column, lab size from 6th column
with open("../data/iie_labs.csv", "r") as f:
    reader = csv.reader(f)
    next(reader, None)  # skip header

    for row in reader:
        lab_name = row[0].lower()
        data[lab_name] = {
            "size": 0,
        }

        # Get lab size (if defined)
        if len(row) >= 7:
            lab_size = row[6]
            data[lab_name]["size"] = lab_size

        # Add empty keywords dict
        for source in sources:
            data[lab_name]["keywords_" + source] = {}


# Load data from each source
for input_file, source in zip(input_files, sources):
    with open(input_file, "r") as f:
        input_data = json.load(f)

    key = "keywords_" + source

    # Get keywords for each lab
    for lab_name, keywords in input_data.items():
        if lab_name not in data:
            print(f"WARNING: {lab_name} not present in iie_labs.csv. Skipping...")
            continue

        data[lab_name][key] = keywords


# Save data
with open(os.path.join(output_dir, output_filename), "w") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
