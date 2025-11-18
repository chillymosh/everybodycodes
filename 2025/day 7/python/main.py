from pathlib import Path

def load_data(file_path: str) -> str:
    data_file = Path(__file__).resolve().parent.parent / file_path
    return data_file.read_text().strip()

def parse_input(data: str) -> tuple[list[str], dict[str, list[str]]]:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    names = lines[0].split(",")
    rules = {
        key: list(values.split(","))
        for line in lines[1:]
        for key, values in (line.split(" > "),)
    }

    return names, rules

def is_valid_name(name: str, rules: dict[str, list[str]]) -> bool:
    for a, b in zip(name, name[1:]):
        allowed = rules.get(a)
        if not allowed or b not in allowed:
            return False
    return True

def find_valid_name(names: list[str], rules: dict[str, list[str]]) -> str | None:
    return next((name for name in names if is_valid_name(name, rules)), None)

def get_valid_indices(names: list[str], rules: dict[str, list[str]]) -> list[int]:
    return [
        i + 1
        for i, name in enumerate(names)
        if is_valid_name(name, rules)
    ]

def extend_prefix(prefix: str, rules: dict[str, list[str]], min_len: int = 7, max_len: int = 11) -> set[str]:
    
    if not is_valid_name(prefix, rules):
        return set()

    results: set[str] = set()

    def dfs(current: str) -> None:
        if min_len <= len(current) <= max_len:
            results.add(current)

        if len(current) == max_len:
            return

        last = current[-1]
        for next_char in rules.get(last, []):
            dfs(current + next_char)

    dfs(prefix)
    return results

def generate_all_names(prefixes: list[str], rules: dict[str, list[str]]) -> set[str]:
    all_names: set[str] = set()
    for prefix in prefixes:
        all_names |= extend_prefix(prefix, rules)
    return all_names


def main() -> None:
    data = load_data("part1.txt")
    names, rules = parse_input(data)

    valid_name = find_valid_name(names, rules)
    print(valid_name)

    data = load_data("part2.txt")
    names, rules = parse_input(data)
    valid_indices = get_valid_indices(names, rules)
    print(sum(valid_indices))
    
    data = load_data("part3.txt")
    prefixes, rules = parse_input(data)
    all_generated = generate_all_names(prefixes, rules)
    print(len(all_generated))


if __name__ == "__main__":
    main()