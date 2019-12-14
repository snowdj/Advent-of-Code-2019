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

    # Iterate over each node and calculate the length to COM.
    for node in orbit_store:
        while orbit_store[node] != 'COM':
            node = orbit_store[node]
            total_length += 1

        total_length += 1

    return total_length


def get_orbit_branch(node, store):
    """Get branch from node to COM."""
    branch = []

    # Calculate entire branch from node to COM.
    while store[node] != 'COM':
        node = store[node] 
        branch.append(node)

    return branch

if __name__ == '__main__':
    # Build orbit store.
    orbit_store = parse_instructions('input.txt')
    
    # Each branch for YOU and SAN.
    YOU_branch = get_orbit_branch('YOU', orbit_store)
    SAN_branch = get_orbit_branch('SAN', orbit_store)

    # Get symmetrical difference between the two branches.
    joined = set(SAN_branch) ^ set(YOU_branch)
    print(len(joined))
