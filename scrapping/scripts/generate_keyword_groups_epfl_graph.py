import os
import csv
import json


input_dir = "../data/scrapped/epfl_graph"
input_file_names = ["keyword_category.csv", "category_category.csv"]
output_dir = "../data/keyword_groups/epfl_graph"


concept_parent = {}
concept_subtrees = {}

for input_file_name in input_file_names:
    input_file_path = os.path.join(input_dir, input_file_name)

    with open(input_file_path, "r") as input_file:
        reader = csv.reader(input_file)
        next(reader)  # skip header

        for row in reader:
            concept = row[0].lower()
            parent = row[1].lower()

            if input_file_name == "keyword_category.csv":
                concept += " (keyword)"  # To avoid conflicts with categories

            concept_parent[concept] = parent

            # Build subtree
            if parent not in concept_subtrees:
                concept_subtrees[parent] = {}

            if concept not in concept_subtrees:
                concept_subtrees[concept] = {}

            concept_subtrees[parent][concept] = concept_subtrees[concept]

# Save data
output_file_path = os.path.join(output_dir, "concept_parent.json")
with open(output_file_path, "w") as output_file:
    json.dump(concept_parent, output_file, indent=4, ensure_ascii=False)


# Build tree
tree = {}
for concept, subtree in concept_subtrees.items():
    # Find roots (concepts without parents)
    if concept in concept_parent:
        continue

    tree[concept] = subtree


# Save data
output_file_path = os.path.join(output_dir, "tree.json")
with open(output_file_path, "w") as output_file:
    json.dump(tree, output_file, indent=4, ensure_ascii=False)
