import csv
import json

import Levenshtein

# List of keywords + corresponding categories from EPFL Graph (unfiltered) #####

reference_pairs = {}

with open("../data/scrapped/epfl_graph/keyword_category_unfiltered.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header

    for row in reader:
        keyword = row[0].lower()
        category = row[1].lower()
        reference_pairs[keyword] = category


# List of keywords from all sources ############################################

keywords_to_classify = set()

# EPFL IIE
paths = [
    "../data/extracted/epfl_graph.json",
    "../data/extracted/epfl_graph_teaching.json",
    "../data/extracted/infoscience.json",
    "../data/scrapped/google_scholar.json",
]

for path in paths:
    with open(path, "r") as f:
        data = json.load(f)

        for lab in data:
            for keyword in data[lab]:
                keywords_to_classify.add(keyword.lower())

# ETHZ

paths = [
    "../../ethz_ifu/data/all_sources.json",
    "../../ethz_usys/data/all_sources.json",
]

for path in paths:
    with open(path, "r") as f:
        data = json.load(f)

        for lab in data:
            for keyword in data[lab]["keywords_research_collection"]:
                keywords_to_classify.add(keyword.lower())


print(f"{len(keywords_to_classify)} keywords to classify")


# Classify keywords ############################################################

new_pairs = {}
print("Classifying keywords...")

for new_keyword in keywords_to_classify:
    if new_keyword in reference_pairs:
        new_pairs[new_keyword] = reference_pairs[new_keyword]
        continue

    # Find nearest keyword or category in references
    best_score = 0  # from 0 to 1
    best_word = None
    best_word_type = None

    for word_list, word_type in zip([reference_pairs.keys(), reference_pairs.values()], ["keyword", "category"]):
        for word in word_list:
            score = Levenshtein.ratio(new_keyword, word)
            if score > best_score:
                best_score = score
                best_word = word
                best_word_type = word_type

    if best_word is None:
        print(f'Could not classify "{new_keyword}"')
        continue

    # Add new pair
    best_category = best_word if best_word_type == "category" else reference_pairs[best_word]
    new_pairs[new_keyword] = best_category

    # print(f"{new_keyword} -> {best_category} \"(matching {best_word}\" with {best_score})")


# Export all pairs #############################################################

print("Exporting in file...")

with open("../data/extracted/keyword_category.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["#keyword", "category"])

    for keyword, category in new_pairs.items():
        writer.writerow([keyword, category])

print("Done")
