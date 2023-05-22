import json


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
        score = round(float(concept_data["edge_Score"]))
        data[lab_name][keyword] = score


# Save data
with open(output_file_path, "w") as output_file:
    json.dump(data, output_file, indent=4, ensure_ascii=False)
