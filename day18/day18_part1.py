import queue
import functools
import collections

SOUND_REGISTER = "__SOUND__"


class Interrupt(Exception):
    pass


def run(program):
    instruction_pointer = 0
    registers = collections.defaultdict(int)
    while (instruction_pointer in range(0, len(program))):
        instruction = program[instruction_pointer]
        try:
            jmp = instruction(registers)
        except Interrupt:
            break
        instruction_pointer += jmp
    return registers


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


def snd(registers, x):
    registers[SOUND_REGISTER] = _translate_arg(registers, x)
    return 1


def set(registers, x, y):
    registers[x] = _translate_arg(registers, y)
    return 1


def add(registers, x, y):
    registers[x] += _translate_arg(registers, y)
    return 1


def mul(registers, x, y):
    registers[x] *= _translate_arg(registers, y)
    return 1


def mod(registers, x, y):
    registers[x] %= _translate_arg(registers, y)
    return 1


def rcv(registers, x):
    if registers[SOUND_REGISTER] != 0:
        registers[x] = registers[SOUND_REGISTER]
        raise Interrupt
    return 1


def jgz(registers, x, y):
    if _translate_arg(registers, x) > 0:
        return _translate_arg(registers, y)
    return 1


def part1():
    print("Test 1 solution is", run(load_program_from_file('test.txt'))[SOUND_REGISTER])
    print("Part 1 solution is", run(load_program_from_file('input.txt'))[SOUND_REGISTER])


if __name__ == "__main__":
    part1()
