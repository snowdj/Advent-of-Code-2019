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
    ABORT = 99
