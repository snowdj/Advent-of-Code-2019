#!/usr/bin/env python3
# -*- coding: utf-8 -*-

start, end = 353096, 843212

passwords = []

for num in range(start, end + 1):
    if str(num) == ''.join(sorted(str(num))) and len(str(num)) != len(set(str(num))):
        passwords.append(num)

print(f'There are {len(passwords)} passwords that meet the criteria.')
