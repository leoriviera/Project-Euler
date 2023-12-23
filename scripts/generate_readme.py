import csv
import urllib.request
from os import listdir
from os.path import isfile, join
from pathlib import Path
from string import Template

PROBLEM_LIST_URL = "https://projecteuler.net/minimal=problems;csv"

# TODO - move this into a config file when there are more languages
languages = {
    "python": {
        "label": "Python",
        "directory": "python/",
    },
}

with urllib.request.urlopen(PROBLEM_LIST_URL) as f:
    lines = f.read().decode("utf-8").strip().split("\r\n")[1:]

    reader = csv.reader(lines)

    problems = {int(row[0]): {"description": row[1], "languages": []} for row in reader}

    for language, info in languages.items():
        directory = info["directory"]

        solved_problems = [
            int(Path(file).stem.split("_")[1])
            for file in listdir(directory)
            if isfile(join(directory, file)) and file.startswith("problem_")
        ]

        for problem in solved_problems:
            problems[problem]["languages"].append(language)

    table = f"|Problem Number|Problem Title|{'|'.join(['Solved in ' + info['label'] + '?' for info in languages.values()])}|\n{'|-' * (len(languages) + 2) + '|'}\n"

    for number, details in problems.items():
        table += f"|[Problem {number}](https://projecteuler.net/problem={number})|{details['description']}|{'|'.join(['✅' if language in details['languages'] else '❌' for language in languages.keys()])}|\n"

    with open("scripts/README_template.md") as t:
        src = Template(t.read())
        result = src.substitute(table=table)

        with open("README.md", "w") as f:
            f.write(result)
