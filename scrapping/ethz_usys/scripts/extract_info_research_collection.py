import csv
import json
import os

# Retrieve profs info
profs = {}
with open("../data/labs.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header

    for row in reader:
        name = f"{row[2]}, {row[3]}"
        lab = row[0]
        institute = row[1]
        profs[name] = {"lab": lab, "institute": institute}


# List scrapped files
input_dir = "../data/scrapped/research_collection"
files = os.listdir(input_dir)


# Create data structure
data = {}

for prof in profs:
    lab = profs[prof]["lab"]
    institute = profs[prof]["institute"]
    data[lab] = {"institute": institute, "keywords_research_collection": {}}


# Extract info
for filename in files:
    filepath = os.path.join(input_dir, filename)

    with open(filepath, "r") as f:
        reader = csv.reader(f)
        header = next(reader)

        affiliation_index = header.index("ethz.leitzahl")
        keywords_index = header.index("dc.subject")

        for row in reader:
            # for i in range(0, len(row)):
            #     col = row[i]
            #     print(i, col)
            # break

            # Find prof name
            affiliations = row[affiliation_index]
            affiliations = affiliations.split("||")

            prof = None
            for prof_test in profs:
                for affiliation in affiliations:
                    if prof_test in affiliation:
                        prof = prof_test
                        break
                if prof:
                    break

            if prof is None:
                unknown_profs = []
                for affiliation in affiliations:
                    affiliation = affiliation.split(" - ")
                    if len(affiliation) > 6:
                        unknown_prof = affiliation[6]
                        if "(emeritus)" not in unknown_prof and "(former)" not in unknown_prof:
                            unknown_profs.append(unknown_prof)
                if unknown_profs:
                    print("Prof not found:", unknown_profs)
                continue

            # Find keywords
            keywords = row[keywords_index].split("||")
            keywords = [keyword.lower() for keyword in keywords]
            if len(keywords) == 1 and keywords[0] == "":
                continue

            # Add to data
            lab = profs[prof]["lab"]
            keywords_lab_dict = data[lab]["keywords_research_collection"]

            for keyword in keywords:
                if keyword not in keywords_lab_dict:
                    keywords_lab_dict[keyword] = 0
                keywords_lab_dict[keyword] += 1

# Save data
output_path = "../data/all_sources.json"
with open(output_path, "w") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
