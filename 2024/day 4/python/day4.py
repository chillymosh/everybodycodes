from pathlib import Path


def process_file(file_name: str, part: int = 1) -> tuple[list[int], int]:
    data_file = Path(__file__).resolve().parent.parent / file_name
    nails = [int(i) for i in data_file.read_text().split() if i.isdigit()]
    return (nails, int(find_median(nails))) if part == 3 else (nails, min(nails))


# Part 1
nails, target = process_file("everybody_codes_e2024_q04_p1.txt")
p1 = sum(n - target for n in nails)
print(p1)

# Part 2
nails, target = process_file("everybody_codes_e2024_q04_p2.txt")
p2 = sum(n - target for n in nails)
print(p2)


# Part 3

# You could also just `from statistics import median`
def find_median(nails: list[int]) -> int:
    nails.sort()
    mid = len(nails) // 2
    if len(nails) % 2 == 0:
        return (nails[mid - 1] + nails[mid]) // 2
    else:
        return nails[mid]


nails, target = process_file("everybody_codes_e2024_q04_p3.txt", 3)
p3 = sum(abs(n - target) for n in nails)
print(p3)
