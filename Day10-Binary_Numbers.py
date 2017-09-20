'''
Day 10: Binary Numbers
Task:
Given a base-10 integer, n, convert it to binary (base-2).
Then find and print the base-10 integer denoting the maximum
number of consecutive 1's in 's binary representation.

Explanation:
Sample Case 1:
The binary representation of 5 is 101, so the maximum number
of consecutive 1's is 1.

Sample Case 2:
The binary representation of 13 is 1101, so the maximum number
of consecutive 1's is 2.
'''

#!/bin/python3

import sys


n = int(input().strip())

count = 0
max_count = 0

while n > 0:
    if n % 2 != 0:
        count += 1
        max_count = max(max_count, count)
    else:
        # reset
        count = 0

    n //= 2

print(max_count)
