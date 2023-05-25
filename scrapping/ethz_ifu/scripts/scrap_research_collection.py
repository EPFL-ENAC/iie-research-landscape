# flake8: noqa
import os
import urllib.request

url_template = "https://www.research-collection.ethz.ch/discover/export?format=csv&rpp=10&etal=0&query=leitzahlCode%3A{code}&scope=/&group_by=none&page=1&sort_by=dc.date.issued_dt&order=desc&filtertype_0=datePublished&filter_relational_operator_0=equals&filter_0={date}"

filename_template = "{date}.csv"
date_start = 2015
date_end = 2023
code = "02608"
output_dir = "../data/scrapped/research_collection"
os.makedirs(output_dir, exist_ok=True)

for date in range(date_start, date_end + 1):
    url = url_template.format(code=code, date=date)
    filename = filename_template.format(date=date)
    print("Downloading", filename)
    urllib.request.urlretrieve(url, os.path.join(output_dir, filename))
