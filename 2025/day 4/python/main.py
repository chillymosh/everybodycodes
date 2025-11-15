from pathlib import Path

def load_data(file_path: str) -> list[str]:
    data_file = Path(__file__).resolve().parent.parent / file_path
    return data_file.read_text().strip().splitlines()

def calculate_gear_ratio(gears: list[str]) -> float:
    ratio = 1.0
    
    for i in range(len(gears) - 1):
        current = gears[i]
        next_gear = gears[i + 1]
        current_teeth = int(current.split('|')[-1]) if '|' in current else int(current)
        next_teeth = int(next_gear.split('|')[0]) if '|' in next_gear else int(next_gear)
        ratio *= current_teeth / next_teeth
    
    return ratio

def main() -> None:
    gears = list(map(int, load_data("part1.txt")))
    turns_first = 2025
    p1 = turns_first * gears[0] // gears[-1]
    print(p1)

    gears = list(map(int, load_data("part2.txt")))
    last_turns = 10_000_000_000_000
    first = gears[0]
    last = gears[-1]
    p2 = (last_turns * last + first - 1) // first
    print(p2)

    gears = load_data("part3.txt")
    turns_first = 100
    ratio = calculate_gear_ratio(gears)
    p3 = int(turns_first * ratio)
    print(p3)
    
if __name__ == "__main__":
    main()
