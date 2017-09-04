'''
Day 3: Intro to Conditional Statements
Task:
Given an integer "n" perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Print Weird if the number is weird; otherwise, print Not Weird.

Explanation

Sample Case 0: n = 3
n is odd and odd numbers are weird, so we print Weird.

Sample Case 1: n = 24
n > 20 and n is even, so it isn't weird. Thus, we print Not Weird.
'''

#!/bin/python3

import sys

N = int(input().strip())

# Checks if N is odd.
if N % 2 != 0:
    print('Weird')
else:
    if (N >= 2 and N <= 5) or N > 20:
        print('Not Weird')
    elif (N >= 6 and N <= 20):
        print('Weird')
