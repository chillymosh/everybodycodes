from collections import Counter
from pathlib import Path

def load_data(file_path: str) -> str:
    data_file = Path(__file__).resolve().parent.parent / file_path
    return data_file.read_text().strip()

def min_number_of_sets(a: list[int]) -> int:
    if not a:
        return 0
    
    counts: dict[int, int] = {}
    for num in a:
        counts[num] = counts.get(num, 0) + 1
    
    return max(counts.values())

def main() -> None:
    data = load_data("part1.txt")
    a = list(map(int, data.split(",")))
    print(sum(set(a)))
    
    data = load_data("part2.txt")
    a = list(map(int, data.split(",")))  
    p2 = sorted(set(a))[:20]
    print(sum(p2))
    
    data = load_data("part3.txt")
    a = list(map(int, data.split(",")))
    freq = Counter(a)
    print(max(freq.values()))
    
    # Or if you don't want to use Counter
    print(min_number_of_sets(a))


if __name__ == "__main__":
    main()