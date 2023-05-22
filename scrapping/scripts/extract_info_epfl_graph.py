import json
import csv


# Research data ################################################################

input_file_path = "../data/scrapped/epfl_graph/lab_keyword.json"
output_file_path = "../data/extracted/epfl_graph.json"

# Saved data
# keys: lab names, values: dict of keywords + occurrences
data = {}


with open(input_file_path, "r") as input_file:
    input_data = json.load(input_file)


for lab_data in input_data:
    lab_name = lab_data["UnitID"].lower()
    data[lab_name] = {}

    # Extract keywords
    for concept_data in lab_data["concept"]:
        keyword = concept_data["PageTitleDisplay"].lower()
        score = float(concept_data["edge_Score"])
        data[lab_name][keyword] = score


# Save data
with open(output_file_path, "w") as output_file:
    json.dump(data, output_file, indent=4, ensure_ascii=False)



# Teaching data ################################################################

input_file_path = "../data/scrapped/epfl_graph/lab_keyword_teaching.csv"
output_file_path = "../data/extracted/epfl_graph_teaching.json"

# Saved data
data = {}

# Import lab names and corresponding SCIPER
labs = {}
with open("../data/iie_labs.csv", "r") as input_file:
    reader = csv.reader(input_file)
    next(reader)  # Skip header

    for row in reader:
        lab_name = row[0].lower()
        sciper = row[1]
        if not sciper:
            continue
        sci = int(sciper)
        labs[str(sciper)] = lab_name


with open(input_file_path, "r") as input_file:
    reader = csv.reader(input_file)
    next(reader)  # Skip header

    for row in reader:
        sciper = int(row[0])
        lab_name = labs[str(sciper)]
        keyword = row[1].lower()
        score = float(row[2])

        if lab_name not in data:
            data[lab_name] = {}

        data[lab_name][keyword] = score


# Save data
with open(output_file_path, "w") as output_file:
    json.dump(data, output_file, indent=4, ensure_ascii=False)
