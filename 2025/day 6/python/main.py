from pathlib import Path
from string import ascii_uppercase

def load_data(file_path: str) -> str:
    data_file = Path(__file__).resolve().parent.parent / file_path
    return data_file.read_text().strip()


def part3(data: str, repeats: int = 1000, distance: int = 1000) -> int:
    ans = 0
    for i in range(repeats):
        if not data[i].isupper():
            ans += data[(-repeats + i) :].count(data[i].upper())

        if not data[-1 - i].isupper():
            ans += data[: (repeats - i)].count(data[-1 - i].upper())

    ans *= distance - 1

    for i in range(len(data)):
        if data[i].isupper():
            continue
        ans += (
            data[max(0, i - repeats) : min(len(data), i + repeats + 1)]
            .count(data[i].upper())
            * distance
        )
    return ans


def main() -> None:
    data = load_data("part1.txt")
    mentor, novice = 0,0
    
    for ch in data:
        mentor += (ch == "A")
        novice += mentor * (ch == "a")
    
    print(novice)

    data = load_data("part2.txt")
    mentors = {c: 0 for c in ascii_uppercase}
    novice = 0

    for ch in data:
        if ch.isupper():
            mentors[ch] += 1
        elif ch.islower():
            novice += mentors[ch.upper()]
    
    print(novice)
    
    data = load_data("part3.txt")
    result = part3(data)
    print(result)


if __name__ == "__main__":
    main()
