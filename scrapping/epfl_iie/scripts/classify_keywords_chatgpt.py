import csv
import json
import os


def create_prompt(categories, keywords):
    prompt = f"""Here is a list of categories, delimited triple backticks and separated by semi-colons:
```
{";".join(categories)}
```

Here is a list of keywords, delimited triple backticks and separated by semi-colons:
```
{";".join(keywords)}
```

Classify each keyword into the best fitting category, chosen from the list of categories.
Don't truncate category names. Don't invent new categories. Don't use another keyword as a category.
Give your answer formatted in JSON, where each key is a keyword and each value is the corresponding category."""

    return prompt


# Classify epfl_graph keywords using snf categories ############################


# Load categories from snf
all_categories = []
categories = []

with open("../data/scrapped/snf/tree_augmented.txt", "r") as f:
    # Read file line by line
    for line in f:
        # Find current level (indented by 2 spaces)
        level = int((len(line) - len(line.lstrip())) / 2)
        line = line.strip().lower()

        all_categories.append(line)
        if level == 2:
            categories.append(line)


# Load keywords from epfl_graph
keywords = []

with open("../data/scrapped/epfl_graph/keyword_category.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header

    for row in reader:
        keywords.append(row[0].lower())


# Generate prompts
n_keywords_per_prompt = 100
prompt_output_dir = "../data/prompts/snf_epfl_graph"
os.makedirs(prompt_output_dir, exist_ok=True)

for i in range(0, len(keywords), n_keywords_per_prompt):
    prompt = create_prompt(categories, keywords[i : i + n_keywords_per_prompt])
    filename = f"prompt_{i}-{i+n_keywords_per_prompt}.txt"
    file_path = os.path.join(prompt_output_dir, filename)
    with open(file_path, "w") as f:
        f.write(prompt)


# Check json answer (saved manually)
try:
    with open("../data/keyword_groups/snf/keyword_category.json", "r") as f:
        answer = json.load(f)

except Exception as e:
    print(e)
    answer = None

if answer:
    wrong_keywords = []
    wrong_categories = set()

    # Check that all keywords are in the answer keys
    for i in range(0, len(keywords)):
        if i >= len(answer.keys()):
            print("answer is missing keywords")
            break

        keyword = keywords[i]

        if keyword not in answer.keys():
            print(f'keyword missing ({i+1}): "{keyword}"')
            wrong_keywords.append(keyword)
            continue

        category = answer[keyword]

        # Check that category exists
        if category not in all_categories:
            print(f'invalid category ({i+1}): "{category}" for keyword "{keyword}"')
            wrong_keywords.append(keyword)
            wrong_categories.add(category)
            continue

    # Generate prompt for wrong keywords
    prompt = create_prompt(categories, wrong_keywords)
    filename = "prompt_wrong_keywords.txt"
    file_path = os.path.join(prompt_output_dir, filename)
    with open(file_path, "w") as f:
        f.write(prompt)

    # Generate prompt for wrong categories
    prompt = create_prompt(categories, wrong_categories)
    filename = "prompt_wrong_categories.txt"
    file_path = os.path.join(prompt_output_dir, filename)
    with open(file_path, "w") as f:
        f.write(prompt)
