#!/usr/bin/env python3
# -*- coding: utf-8 -*-

start, end = 353096, 843212

passwords = [password for password in (
                str(number) for number in range(start, end + 1)) 
                if (
                    any(
                        str(digit) * 2 in password and str(digit) * 3 not in password 
                        for digit in '0123456789'
                    ) and
                    ''.join(sorted(password)) == password)]
                
print(f'There are {len(passwords)} passwords that meet the criteria.')
