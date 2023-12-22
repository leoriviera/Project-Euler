import csv
import urllib.request

PROBLEM_LIST_URL = "https://projecteuler.net/minimal=problems;csv"

with urllib.request.urlopen(PROBLEM_LIST_URL) as f:
    lines = f.read().decode("utf-8").strip().split("\r\n")[1:]

    reader = csv.reader(lines)

    problems = { int(row[0]): { "description": row[1], "languages": [] } for row in reader }

    print(problems)
