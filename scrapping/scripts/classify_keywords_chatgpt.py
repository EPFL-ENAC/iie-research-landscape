import csv
import json

# import openai

# openai.api_key  = os.getenv("OPENAI_API_KEY")

# From https://learn.deeplearning.ai/chatgpt-prompt-eng/
# def get_completion(prompt, model="gpt-3.5-turbo"):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0, # this is the degree of randomness of the model's output
#     )
#     return response.choices[0].message["content"]


def create_prompt(categories, keyword):
    prompt = f"""Here is a list of categories, delimited triple backticks and separated by semi-colons:
```
{" ; ".join(categories)}
```

{create_short_prompt(keyword)}"""

    return prompt


def create_short_prompt(keyword):
    prompt = f"""Find the category from the list that best fit the keyword ```{keyword}```.
Only use full and precise category names. Do not make up new categories.
Give your answer as a single category in lowercase and delimited by tripple backticks."""

    return prompt


# Classify epfl_graph keywords using snf categories ############################


# Load categories from snf
categories = []

with open("../data/scrapped/snf/tree.txt", "r") as f:
    # Read file line by line
    for line in f:
        # Find current level (indented by 2 spaces)
        level = int((len(line) - len(line.lstrip())) / 2)
        line = line.strip().lower()

        if level == 2:
            categories.append(line)


# Load keywords from epfl_graph
keywords = []

with open("../data/scrapped/epfl_graph/keyword_category.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header

    for row in reader:
        keywords.append(row[0].lower())


# Generate prompts and answers
# keyword_category = {}

# for i in range(len(keywords)):
#     keyword = keywords[i]

#     prompt = create_prompt(categories, keyword)
#     response = None
#     while not response:
#         try:
#             response = get_completion(prompt)
#         except:
#             pass

#     # Isolate category from response
#     start_index = response.find("```") + 3
#     end_index = response.find("```", start_index)
#     category = response[start_index:end_index]
#     print(f'"({i}){keyword}": "{category}",')
#     keyword_category[keyword] = category


# Check json answer (saved manually)
try:
    with open("../data/keyword_groups/snf/keyword_category.json", "r") as f:
        answer = json.load(f)

except Exception as e:
    print(e)
    answer = None

if answer:
    wrong_keywords = []

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

        # Check that category exists
        if answer[keyword] not in categories:
            print(f'invalid category ({i+1}): "{answer[keyword]}" for keyword "{keyword}"')
            wrong_keywords.append(keyword)
            continue
