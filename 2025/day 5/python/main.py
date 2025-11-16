from pathlib import Path

def load_data(file_path: str) -> str:
    data_file = Path(__file__).resolve().parent.parent / file_path
    return data_file.read_text().strip()

def build_spine(values: list[int]) -> tuple[int, list[list[int | None]]]:
    spine: list[list[int | None]] = [[values[0], None, None]]

    for x in values[1:]:
        for seg in spine:
            if seg[0] is not None and x < seg[0] and seg[1] is None:
                seg[1] = x
                break
            if seg[0] is not None and x > seg[0] and seg[2] is None:
                seg[2] = x
                break
        else:
            spine.append([x, None, None])

    quality = int(''.join(str(seg[0]) for seg in spine))
    return quality, spine

def get_levels(spine: list[list[int | None]]) -> list[int]:
    return [int(''.join(str(x) for x in row if x is not None)) for row in spine]

def main() -> None:
    data = load_data("part1.txt")
    _, quality_str = data.split(":")
    values = list(map(int, quality_str.split(",")))
    quality, _ = build_spine(values)
    print(quality)

    data = load_data("part2.txt")
    qualities: list[int] = []
    for line in data.splitlines():
        _, quality_str = line.split(":")
        values = list(map(int, quality_str.split(",")))
        quality, _ = build_spine(values)
        qualities.append(quality)
    print(max(qualities) - min(qualities))
    
    data = load_data("part3.txt")
    swords: list[tuple[int, int, list[int]]] = []
    for line in data.splitlines():
        uid_str, quality_str = line.split(":")
        uid = int(uid_str)
        values = list(map(int, quality_str.split(",")))
        quality, spine = build_spine(values)
        levels = get_levels(spine)
        swords.append((uid, quality, levels))
    
    swords.sort(key=lambda x: (x[1], x[2], x[0]), reverse=True)
    
    checksum = sum((position + 1) * uid for position, (uid, _, _) in enumerate(swords))
    print(checksum)

if __name__ == "__main__":
    main()