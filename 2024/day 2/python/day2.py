import itertools
from pathlib import Path
from collections import defaultdict

# Part 1
words = ["LOR", "LL", "SI", "OR", "ET", "IT", "ON"]
inscriptions = "LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT, SED DO EIUSMOD TEMPOR INCIDIDUNT UT LABORE ET DOLORE MAGNA ALIQUA. UT ENIM AD MINIM VENIAM, QUIS NOSTRUD EXERCITATION ULLAMCO LABORIS NISI UT ALIQUIP EX EA COMMODO CONSEQUAT. DUIS AUTE IRURE DOLOR IN REPREHENDERIT IN VOLUPTATE VELIT ESSE CILLUM DOLORE EU FUGIAT NULLA PARIATUR. EXCEPTEUR SINT OCCAECAT CUPIDATAT NON PROIDENT, SUNT IN CULPA QUI OFFICIA DESERUNT MOLLIT ANIM ID EST LABORUM."

p1 = sum(inscriptions.count(word) for word in words)
print(p1)

# Part 2

data_file = Path(__file__).resolve().parent.parent / "everybody_codes_e2024_q02_p2.txt"
data = data_file.read_text().strip()
header, text = data.split("\n\n")
words = set(header.replace("WORDS:", "").split(","))
words.update({w[::-1] for w in words})

p2 = 0
for word in text.splitlines():
    indexes: set[int] = set()
    for keyword in words:
        start = 0
        while (start := word.find(keyword, start)) != -1:
            indexes.update(range(start, start + len(keyword)))
            start += 1
    p2 += len(indexes)
print(p2)


# Part 3

data_file = Path(__file__).resolve().parent.parent / "everybody_codes_e2024_q02_p3.txt"
data = data_file.read_text().strip()
header, text = data.split("\n\n")
words = set(header.replace("WORDS:", "").split(","))
words.update({w[::-1] for w in words})
grid = [list(row) for row in text.splitlines()]

unique_indices: set[tuple[int, int]] = set()

grid_height = len(grid)
grid_width = len(grid[0])

words_by_length: dict[int, list[str]] = defaultdict(list)
for word in words:
    words_by_length[len(word)].append(word)

unique_indices: set[tuple[int, int]] = set()

for word_length, word_list in words_by_length.items():
    for y, x in itertools.product(range(grid_height), range(grid_width)):
        if word_length <= grid_width:
            h_slice = "".join(grid[y][(x + i) % grid_width] for i in range(word_length))
            for word in word_list:
                if h_slice == word:
                    unique_indices.update(
                        (y, (x + i) % grid_width) for i in range(word_length)
                    )

        if y + word_length <= grid_height:
            v_slice = "".join(grid[y + i][x] for i in range(word_length))
            for word in word_list:
                if v_slice == word:
                    unique_indices.update((y + i, x) for i in range(word_length))

p3 = len(unique_indices)
print(p3)


# Alternative way but slower
for y, x in itertools.product(range(grid_height), range(grid_width)):
    for word in words:
        word_length = len(word)

        if y + word_length <= grid_height and all(
            grid[y + i][x] == word[i] for i in range(word_length)
        ):
            unique_indices.update((y + i, x) for i in range(word_length))

        if all(grid[y][(x + i) % grid_width] == word[i] for i in range(word_length)):
            unique_indices.update((y, (x + i) % grid_width) for i in range(word_length))

p3 = len(unique_indices)
