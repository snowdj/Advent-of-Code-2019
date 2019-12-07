#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""Intcode computer."""

from modes import modes
from opcodes import opcodes


def digest_input():
    """Read a text file into a list."""
    with open('input.txt') as f:
        for count, line in enumerate(f):
            return [int(i) for i in line.split(',')]


def read(memory, index, offset, mode):
    """Read an item from memory."""
    item = memory[index + offset]

    if mode == modes.POSITION:
        item = memory[item]
    return item


def write(memory, index, offset, value):
    """Write an item to memory."""
    memory[memory[index + offset]] = value


def run(memory):
    """Process an intcode instruction."""
    i = 0
    while i < len(memory):
        # Get opcode and parameter modes.
        opcode = memory[i] % 100
        p_mode1 = memory[i] // 100 % 10
        p_mode2 = memory[i] // 1000 % 10
        p_mode3 = memory[i] // 10000

        if opcode == opcodes.ADD:
            param1 = read(memory, i, 1, p_mode1)
            param2 = read(memory, i, 2, p_mode2)
            param3 = read(memory, i, 3, p_mode3)
            write(memory, i, 3, param1 + param2)
            i += 4
        elif opcode == opcodes.MULTIPLY:
            param1 = read(memory, i, 1, p_mode1)
            param2 = read(memory, i, 2, p_mode2)
            param3 = read(memory, i, 3, p_mode3)
            write(memory, i, 3, param1 * param2)
            i += 4
        elif opcode == opcodes.GET:
            user_input = int(input('>: '))
            write(memory, i, 1, user_input)
            i += 2
        elif opcode == opcodes.PRINT:
            print(read(memory, i, 1, p_mode1))
            i += 2
        elif opcode ==opcodes.ABORT:
            return
        else:
            print(f'Unrecognized opcode: {opcode}.')


if __name__ == '__main__':
    """Main."""
    memory = digest_input()
    run(memory)
