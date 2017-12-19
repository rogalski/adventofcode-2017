import string
import collections
from typing import List, Tuple

LETTERS = set(string.ascii_uppercase)

UP, DOWN, LEFT, RIGHT = 'UDLR'
MOVE = {
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1)
}
CHANGE_DIRECTION = {
    DOWN: [LEFT, RIGHT],
    UP: [LEFT, RIGHT],
    LEFT: [UP, DOWN],
    RIGHT: [UP, DOWN]
}

Traversal = collections.namedtuple('Traversal', ['letters', 'steps'])


def map_from_string(string: str) -> List[List[str]]:
    return [list(line) for line in string.splitlines()]


def map_from_file(file_name: str) -> List[List[str]]:
    with open(file_name) as fh:
        return [list(line) for line in fh]


def traverse(map: List[List[str]]) -> Traversal:
    encountered_letters = []
    row, col = find_starting_point(map)
    direction = DOWN
    steps_count = 1
    while True:
        if map[row][col] in LETTERS:
            encountered_letters.append(map[row][col])
        row, col, direction = get_next_step(map, row, col, direction)
        if map[row][col] == " ":
            break  # end of traverse
        steps_count += 1

    return Traversal("".join(encountered_letters), steps_count)


def get_next_step(map, row, col, direction):
    if map[row][col] == '+':
        for candidate in CHANGE_DIRECTION[direction]:
            dx, dy = MOVE[candidate]
            try:
                tile = map[row + dx][col + dy]
                if tile != ' ':
                    return row + dx, col + dy, candidate
            except IndexError:
                continue
        raise ValueError
    else:
        dx, dy = MOVE[direction]
        return row + dx, col + dy, direction


def find_starting_point(map: List[List[str]]) -> Tuple[int, int]:
    first_row = map[0]
    for col, char in enumerate(first_row):
        if char == '|':
            return 0, col
    raise ValueError


if __name__ == "__main__":
    traversal = traverse(map_from_file("input.txt"))
    print("Part 1 soluton is", traversal.letters)
    print("Part 2 soluton is", traversal.steps)
