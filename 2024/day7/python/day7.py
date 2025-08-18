from pathlib import Path


data_file = Path(__file__).resolve().parent.parent / "everybody_codes_e2024_q07_p1.txt"
data = data_file.read_text().strip()

d: dict[str, list[str]] = {}
for line in data.splitlines():
    key, vals = line.split(":")
    d[key] = vals.split(",")


def calculate_total_essence(
    actions: list[str], segments: int = 10, start_power: int = 10
) -> int:
    actions_len = len(actions)
    power = start_power
    total_essence = 0

    for i in range(segments):
        action = actions[i % actions_len]
        if action == "+":
            power += 1
        elif action == "-" and power > 0:
            power -= 1
        total_essence += power

    return total_essence


results = {plan: calculate_total_essence(actions) for plan, actions in d.items()}
sorted_plans = sorted(results.items(), key=lambda x: x[1], reverse=True)
sorted_plan_names = [plan[0] for plan in sorted_plans]

print("Part 1:", "".join(sorted_plan_names))


def unique_permutations(seq):
    counter = Counter(seq)

    def generate_perms(elements, path=[]):
        if len(path) == len(seq):
            yield tuple(path)
            return
        for elem in elements:
            if elements[elem] > 0:
                elements[elem] -= 1
                yield from generate_perms(elements, path + [elem])
                elements[elem] += 1

    return generate_perms(counter)


perms = set(unique_permutations("+++++---==="))
