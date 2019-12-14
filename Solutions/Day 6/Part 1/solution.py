#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Orbit count checksum."""

import json

def parse_instructions(file):
    """Parse an instruction file."""
    # Store for orbits.
    store = {}

    # Read input file and parse parent/child.
    with open(file, 'r') as f:
        # Iterate over each line of the input file.
        for count, line in enumerate(f):
            # Cleanup each line
            orbit = [parent.replace('\n', '') for parent in line.split(')')]

            # Give fancy names to each piece of the orbit.
            parent = orbit[1]
            child = orbit[0]

            # Create the key in the orbit store if it doesn't exist.
            if parent not in store.keys():
                store[parent] = []
                
            # Stash the orbit.
            store[parent] = child

    return store

def count_orbits():
    """Calculate the total length of all orbit transfer branches."""
    orbit_store = parse_instructions('input.txt')
    total_length = 0
    for node in orbit_store:
        while orbit_store[node] != 'COM':
            node = orbit_store[node]
            total_length += 1

        total_length += 1

    return total_length

if __name__ == '__main__':
    print(f'Total length of all orbit branches: {count_orbits()}.')
