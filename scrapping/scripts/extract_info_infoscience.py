import csv
import json
import os
import xml.etree.ElementTree as ET

# Saved data
# keys: lab names, values: dict of keywords + occurrences
data = {}

# load list of labs for filtering
# only keep first column (lab names)
with open("../data/iie_labs.csv", "r") as f:
    reader = csv.reader(f)
    next(reader, None)  # skip header
    iie_labs = [row[0] for row in reader]
iie_labs = [lab.lower() for lab in iie_labs]

# list xml files
input_dir = "../data/scrapped/infoscience"
xml_files = [f for f in os.listdir(input_dir) if f.endswith(".xml")]

# iterate over xml files
for xml_file in xml_files:
    print("Processing file: " + xml_file)

    # parse the XML file
    tree = ET.parse(os.path.join(input_dir, xml_file))
    root = tree.getroot()
    namespace = root.tag.split("}")[0].strip("{")
    ns = {"": namespace}

    # loop through all the <record> elements
    records = root.findall("record", ns)
    for i, record in enumerate(records):
        # extract laboratory name
        lab_names = record.findall('.//datafield[@tag="909"]/subfield[@code="p"]', ns)
        lab_names = [lab_name.text for lab_name in lab_names]
        lab_names = [lab_name.lower() for lab_name in lab_names]
        lab_names = [lab_name for lab_name in lab_names if lab_name in iie_labs]

        # extract authors' names
        # author_names = record.findall('.//datafield[@tag="700"]/subfield[@code="a"]', ns)
        # author_names = [author_name.text for author_name in author_names]

        # extract keywords
        keywords = record.findall('.//datafield[@tag="653"]/subfield[@code="a"]', ns)
        keywords = [keyword.text for keyword in keywords]
        keywords = [keyword.lower() for keyword in keywords]

        # print(f"{i+1}/{len(records)}")
        # print("Labs:     ", ", ".join(lab_names))
        # print("Keywords: ", ", ".join(keywords))
        # print()

        for lab_name in lab_names:
            if lab_name not in data:
                data[lab_name] = {}

            for keyword in keywords:
                if keyword not in data[lab_name]:
                    data[lab_name][keyword] = 0
                data[lab_name][keyword] += 1


# Export data as json
output_dir = "../data/extracted"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "infoscience.json")

with open(output_path, "w") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
