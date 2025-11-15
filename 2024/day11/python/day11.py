from pathlib import Path

def load_data(file_path: str) -> dict[str, list[str]]:
    data_file = Path(__file__).resolve().parent.parent / file_path
    d: dict[str, list[str]] = {}
    for line in data_file.read_text().strip().splitlines():
        k, v = line.split(":")
        d[k] = v.split(",")
    return d


def calc_population(notes: dict[str, list[str]], days: int, initial: str) -> int:
    population_count = {termite: 0 for termite in notes}
    population_count[initial] = 1

    for _ in range(days):
        new_population_count = {termite: 0 for termite in notes}
        for termite, count in population_count.items():
            for converted in notes[termite]:
                new_population_count[converted] += count
        population_count = new_population_count
    return sum(population_count.values())

p1 = calc_population(load_data("part1.txt"), 4, "A")
print(p1)

p2 = calc_population(load_data("part2.txt"), 10, "Z")
print(p2)

notes = load_data("part3.txt")
populations = [calc_population(notes, 20, t) for t in notes]
p3 = max(populations) - min(populations)
print(p3)
