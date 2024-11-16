from pathlib import Path


def adjacent(coord: tuple[int, int], part_no: int) -> list[tuple[int, int]]:
    r, c = coord
    directions = [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]
    if part_no == 3:
        directions.extend(
            [(r - 1, c + 1), (r + 1, c + 1), (r + 1, c - 1), (r - 1, c - 1)]
        )
    return directions


def dig(queue: list[tuple[int, int]], part_no: int) -> list[tuple[int, int]]:
    return [
        coord
        for coord in queue
        if all((r, c) in queue for r, c in adjacent(coord, part_no))
    ]


def begin_dig(input_data: str, part_no: int) -> int:
    queue = [
        (ix, yx)
        for ix, row in enumerate(input_data.splitlines())
        for yx, cell in enumerate(row)
        if cell != "."
    ]

    counter = len(queue)

    while queue:
        queue = dig(queue, part_no)
        counter += len(queue)

    return counter


def process_file(file_name: str, part_no: int = 1) -> int:
    data_file = Path(__file__).resolve().parent.parent / file_name
    input_data = data_file.read_text().strip()
    return begin_dig(input_data, part_no)


p1 = process_file("everybody_codes_e2024_q03_p1.txt")
print(p1)

p2 = process_file("everybody_codes_e2024_q03_p2.txt")
print(p2)

p3 = process_file("everybody_codes_e2024_q03_p3.txt", 3)
print(p3)
