from pathlib import Path
from collections import defaultdict
from functools import lru_cache
import itertools


def load_data(file_path: str) -> list[str]:
    data_file = Path(__file__).resolve().parent.parent / file_path
    return data_file.read_text().strip().splitlines()

def process_data(data: list[str]) -> defaultdict[str, list[str]]:
    d: dict[str, list[str]] = defaultdict(list)
    for line in data:
        start, paths = line.split(":")
        d[start].extend(paths.split(","))
    return d

data = load_data("everybody_codes_e2024_q06_p1.txt")
d = process_data(data)

@lru_cache(maxsize=128)
def find_paths(root: str) -> list[list[str]]:
    if root in {"BUG", "ANT"}:
        return []
    if root == "@":
        return [["@"]]
    return [[root] + p for c in d[root] for p in find_paths(c)]

# Part 1

paths = find_paths("RR")
paths.sort(key=len)
for length, group in itertools.groupby(paths, key=len):
    group = list(group)
    if len(group) == 1:
        print("".join(group[0]))

# Part 2

data = load_data("everybody_codes_e2024_q06_p2.txt")
d = process_data(data)
find_paths.cache_clear()
paths = find_paths("RR")
paths.sort(key=len)
for length, group in itertools.groupby(paths, key=len):
    group = list(group)
    if len(group) == 1:
        print("".join(g[0] for g in group[0]))

# Part 3

data = load_data("everybody_codes_e2024_q06_p3.txt")
d = process_data(data)
find_paths.cache_clear()
paths = find_paths("RR")
paths.sort(key=len)
for length, group in itertools.groupby(paths, key=len):
    group = list(group)
    if len(group) == 1:
        print("".join(g[0] for g in group[0]))


