from pathlib import Path


def load_data(file_path: str) -> list[str]:
    data_file = Path(__file__).resolve().parent.parent / file_path
    return data_file.read_text().strip().splitlines()

def format_data(data: list[str]) -> tuple[list[str], list[str]]:
    names = data[0]
    instructions = data[-1]
    return names.split(","), instructions.split(",")

def parse_instruction(inst: str) -> tuple[str, int]:
    return inst[0], int(inst[1:])

def p1(names: list[str], instructions: list[str]) -> str:
    idx = 0

    for inst in instructions:
        d, steps = parse_instruction(inst)
        idx = max(0, idx - steps) if d == "L" else min(len(names) - 1, idx + steps)

    return names[idx]

def p2(names: list[str], instructions: list[str]) -> str:
    idx, n = 0, len(names)

    for inst in instructions:
        d, steps = parse_instruction(inst)

        idx = (idx + steps) % n if d == "R" else (idx - steps) % n

    return names[idx]

def p3(names: list[str], instructions: list[str]) -> str:
    names, n = names[:], len(names)

    for inst in instructions:
        d, steps = parse_instruction(inst)
        idx = (steps if d == "R" else -steps) % n
        names[0], names[idx] = names[idx], names[0]

    return names[0]

def main() -> None:
    data = load_data("part1.txt")
    names, instructions = format_data(data)
    print(p1(names, instructions))

    data = load_data("part2.txt")
    names, instructions = format_data(data)
    print(p2(names, instructions))

    data = load_data("part3.txt")
    names, instructions = format_data(data)
    print(p3(names, instructions))


if __name__ == "__main__":
    main()
