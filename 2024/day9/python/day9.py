from pathlib import Path

dots = (1, 3, 5, 10)

def load_data(file_path: str) -> list[int]:
    data_file = Path(__file__).resolve().parent.parent / file_path
    return list(map(int, data_file.read_text().strip().splitlines()))


def calc_min_dots(num: int, dots: tuple[int,...]) -> float:
    INF = float('inf')
    min_dots = [INF] * (num + 1)
    min_dots[0] = 0 

    for amount in range(1, num + 1):
        for dot in dots:
            if dot <= amount:
                min_dots[amount] = min(min_dots[amount], min_dots[amount - dot] + 1)

    return min_dots[num]

notes = load_data("part1.txt")
p1 = sum(calc_min_dots(b, dots) for b in notes)
print(p1)

dots = (1, 3, 5, 10, 15, 16, 20, 24, 25, 30)
notes = load_data("part2.txt")
p2 = sum(calc_min_dots(b, dots) for b in notes)
print(p2)

def find_optimal_split(brightness: int, dots: tuple[int,...]) -> tuple[float, float, tuple[int, int]] | tuple[float, float, None]:
    min_dots = [float('inf')] * (brightness + 1)
    min_dots[0] = 0

    for amount in range(1, brightness + 1):
        for dot in dots:
            if dot <= amount:
                min_dots[amount] = min(min_dots[amount], min_dots[amount - dot] + 1)


    best_split = None
    min_total_beetles = float('inf')

    for i in range((brightness // 2) + 1):
        j = brightness - i
        if abs(i - j) <= 100:
            total_beetles = min_dots[i] + min_dots[j]
            if total_beetles < min_total_beetles:
                min_total_beetles = total_beetles
                best_split = (i, j)
    if best_split:
        return (min_dots[best_split[0]], min_dots[best_split[1]], best_split)
    else:
        return (float('inf'), float('inf'), None)



total_beetles = 0
dots = (1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101)
notes = load_data("part3.txt")
for brightness in notes:
    beetles1, beetles2, split = find_optimal_split(brightness, dots)
    total_beetles += beetles1 + beetles2

print(f"Total beetles required: {total_beetles}")