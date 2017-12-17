import collections


class Spinlock:
    def __init__(self, step_size: int):
        self.buffer = collections.deque([0])
        self.pointer = 0
        self._step_size = step_size
        self._last_value = 0

    def insert(self):
        value_to_insert = self._last_value + 1
        new_position = (self.pointer + self._step_size) % value_to_insert + 1
        self.buffer.insert(new_position, value_to_insert)
        self.pointer = new_position
        self._last_value = value_to_insert

    def spin(self, n):
        for _ in range(n):
            self.insert()


def spinlock0(step_size, spin_count):
    pointer = 0
    value_after_0 = None
    for n in range(1, spin_count + 1):
        pointer = (pointer + step_size) % n
        if pointer == 0:
            value_after_0 = n
        pointer += 1
    return value_after_0


def part1():
    s = Spinlock(step_size=343)
    s.spin(2017)
    p_2017 = s.buffer.index(2017)
    print("Part 1 solution is", s.buffer[p_2017 + 1])


def part2():
    print("Part 2 solution is", spinlock0(343, 50_000_000))


if __name__ == "__main__":
    part1()
    part2()
