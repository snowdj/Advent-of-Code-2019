#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Opcode class."""

from enum import IntEnum


class opcodes(IntEnum):
    """Opcodes for intcode."""

    ADD = 1,
    MULTIPLY = 2,
    GET = 3,
    PRINT = 4,
    JUMP_IF_TRUE = 5,
    JUMP_IF_FALSE = 6,
    LESS_THAN = 7,
    EQUALS = 8,
    ABORT = 99
