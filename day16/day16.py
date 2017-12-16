import functools
from typing import List, Iterable, Iterator, Callable

PROGRAM_NAMES = 'abcdefghijklmnop'


def shift(positions: List[str], size: int):
    positions[:] = positions[-size:] + positions[:-size]


def swap_by_index(positions: List[str], i1: int, i2: int):
    positions[i1], positions[i2] = positions[i2], positions[i1]


def swap_by_value(positions: List[str], v1: str, v2: str):
    d = {v: i for i, v in enumerate(positions)}
    swap_by_index(positions, d[v1], d[v2])


def dance_steps_from_file(file_name: str) -> Iterator[Callable]:
    with open(file_name) as fh:
        steps_strings = fh.read().split(',')
    return map(to_step, steps_strings)


def to_step(s: str) -> Callable:
    if s[0] == 's':
        size = int(s[1:])
        return functools.partial(shift, size=size)
    elif s[0] == 'x':
        i1, i2 = map(int, s[1:].split('/'))
        return functools.partial(swap_by_index, i1=i1, i2=i2)
    elif s[0] == 'p':
        v1, v2 = s[1:].split('/')
        return functools.partial(swap_by_value, v1=v1, v2=v2)
    else:
        raise ValueError


def dance_once(positions: List[str], steps: Iterable[Callable]) -> List[str]:
    positions = list(positions)
    for s in steps:
        s(positions)
    return positions


def initial_positions(program_count: int) -> List[str]:
    return list(PROGRAM_NAMES[:program_count])


def to_string(p: List[str]) -> str:
    return ''.join(p)


def brent(f, x0):
    """
    Brent cycle detection algorithm taken from Wiki
    Some stuff is renamed fgor better understanding
    :param f: function in which se search for cyc;e
    :param x0:
    :return:
    """
    # search successive powers of two until upper bound of cycle is found
    upperCycleBound = cycle = 1
    tortoise = x0
    hare = f(x0)  # f(x0) is the next element
    while tortoise != hare:
        if upperCycleBound == cycle:  # time to start a new power of two?
            tortoise = hare
            upperCycleBound *= 2
            cycle = 0
        hare = f(hare)
        cycle += 1

    # Find the position of the first repetition of length λ
    firstEncounter = 0
    tortoise = hare = x0
    for i in range(cycle):
        # range(cycle) produces a list with the values 0, 1, ... , cycle-1
        hare = f(hare)
    # The distance between the hare and tortoise is now λ.

    # Next, the hare and tortoise move at same speed until they agree
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        firstEncounter += 1

    return cycle, firstEncounter


def part1():
    p = initial_positions(16)
    for step in dance_steps_from_file("input.txt"):
        step(p)

    print("Part 1 solution is", to_string(p))


def part2():
    # All right, I needed to read a little bit about it
    # https://en.wikipedia.org/wiki/Cycle_detection
    #
    # For any function f that maps a finite set S to itself, and any initial value x0 in S,
    # the sequence of iterated function values must eventually use the same value twice:
    # there must be some pair of distinct indices i and j such that xi = xj.
    # Once this happens, the sequence must continue periodically, by repeating the same
    # sequence of values from xi to xj − 1. Cycle detection is the problem of finding
    # i and j, given f and x0.

    steps = list(dance_steps_from_file("input.txt"))
    f = functools.partial(dance_once, steps=steps)
    p0 = initial_positions(16)
    cycle, offset = brent(f, p0)
    N = 1_000_000_000
    n = (N - offset) % cycle + offset
    print("Cycles count reduced to", n)

    positions = initial_positions(16)
    for _ in range(n):
        for s in steps:
            s(positions)

    print("Part 2 solution is", to_string(positions))


if __name__ == "__main__":
    part1()
    part2()