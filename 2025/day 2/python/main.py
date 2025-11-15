import ast
from pathlib import Path

def load_data(file_path: str) -> str:
    data_file = Path(__file__).resolve().parent.parent / file_path
    return data_file.read_text().strip()

def add(a: list[int], b: list[int]) -> list[int]:
    return [a[0] + b[0], a[1] + b[1]]

def multiply(a: list[int], b: list[int]) -> list[int]:
    return [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]]

def divide(a: list[int], b: list[int]) -> list[int]:
    return [int(a[0] // b[0]), int(a[1] / b[1])]

def p1(a: list[int]) -> list[int]:
    r = [0,0]
    for _ in range(3):
        r = multiply(r, r)
        r = divide(r, [10,10])
        r = add(r, a)
    return(r)  

def p2(a: list[int]) -> int:
    ax, ay = a
    count = 0

    for dx in range(0, 1001, 10):
        for dy in range(0, 1001, 10):
            px = ax + dx
            py = ay + dy
            rx, ry = 0, 0
            engraved = True

            for _ in range(100):
                rx_new = rx * rx - ry * ry
                ry_new = 2 * ry * rx
                rx = int(rx_new / 100000) + px
                ry = int(ry_new / 100000) + py
                
                if abs(rx) > 1_000_000 or abs(ry) > 1_000_000:
                    engraved = False
                    break

            if engraved:
                count += 1

    return count

def p3(a: list[int]) -> int:
    ax, ay = a
    count = 0

    for dx in range(1001):
        px = ax + dx
        for dy in range(1001):
            py = ay + dy
            rx, ry = 0, 0

            for _ in range(100):
                rx_new = rx * rx - ry * ry
                ry_new = 2 * rx * ry
                rx = int(rx_new / 100000) + px
                ry = int(ry_new / 100000) + py
                
                if abs(rx) > 1_000_000 or abs(ry) > 1_000_000:
                    break
            else:
                count += 1

    return count


def main() -> None:
    raw = load_data("part1.txt").partition("=")[-1].strip()
    a = ast.literal_eval(raw)
    print(p1(a))

    raw = load_data("part2.txt").partition("=")[-1].strip()
    a = ast.literal_eval(raw)
    print(p2(a))

    raw = load_data("part3.txt").partition("=")[-1].strip()
    a = ast.literal_eval(raw)
    print(p3(a))

    
if __name__ == "__main__":
    main()
