import functools
import collections

RUNNING = 'RUNNING'
DONE = 'DONE'
QUEUE_EMPTY = 'QUEUE_EMPTY'


class Program:
    def __init__(self, code, output_queue, input_queue):
        self._code = code
        self.output_queue = output_queue
        self.input_queue = input_queue

        self._instruction_pointer = 0
        self.registers = collections.defaultdict(int)

        self.snd_count = 0
        self.rcv_count = 0

    def step(self):
        try:
            instruction = self._code[self._instruction_pointer]
        except IndexError:
            return DONE

        try:
            jmp = instruction(self)
        except IndexError:  # propagated from deque
            return QUEUE_EMPTY
        else:
            self._instruction_pointer += jmp
            return RUNNING


def load_program_from_file(filename):
    with open(filename) as fh:
        return [line_to_instruction(line) for line in fh]


def line_to_instruction(line):
    instr, *args = line.split()
    if instr == 'snd':
        return functools.partial(snd, x=args[0])
    elif instr == 'set':
        return functools.partial(set, x=args[0], y=args[1])
    elif instr == 'add':
        return functools.partial(add, x=args[0], y=args[1])
    elif instr == 'mul':
        return functools.partial(mul, x=args[0], y=args[1])
    elif instr == 'mod':
        return functools.partial(mod, x=args[0], y=args[1])
    elif instr == 'rcv':
        return functools.partial(rcv, x=args[0])
    elif instr == 'jgz':
        return functools.partial(jgz, x=args[0], y=args[1])
    else:
        raise ValueError


def _translate_arg(registers, arg):
    try:
        return int(arg)
    except ValueError:
        return registers[arg]


def snd(self, x):
    self.snd_count += 1
    self.output_queue.append(_translate_arg(self.registers, x))
    return 1


def set(self, x, y):
    self.registers[x] = _translate_arg(self.registers, y)
    return 1


def add(self, x, y):
    self.registers[x] += _translate_arg(self.registers, y)
    return 1


def mul(self, x, y):
    self.registers[x] *= _translate_arg(self.registers, y)
    return 1


def mod(self, x, y):
    self.registers[x] %= _translate_arg(self.registers, y)
    return 1


def rcv(self, x):
    self.rcv_count += 1
    self.registers[x] = self.input_queue.popleft()
    return 1


def jgz(self, x, y):
    if _translate_arg(self.registers, x) > 0:
        return _translate_arg(self.registers, y)
    return 1


def run_together(program):
    queue_0_1 = collections.deque()
    queue_1_0 = collections.deque()
    p0 = Program(program, queue_0_1, queue_1_0)
    p0.registers['p'] = 0
    p1 = Program(program, queue_1_0, queue_0_1)
    p1.registers['p'] = 1
    while True:
        state0 = p0.step()
        state1 = p1.step()
        # print(p0.registers, p1.registers, queue_0_1, queue_1_0)
        if state0 != RUNNING and state1 != RUNNING:
            break
    return p1.snd_count

def part2():
    print("Test 2 solution is", run_together(load_program_from_file('test2.txt')))
    print("Part 2 solution is", run_together(load_program_from_file('input.txt')))


if __name__ == "__main__":
    part2()
