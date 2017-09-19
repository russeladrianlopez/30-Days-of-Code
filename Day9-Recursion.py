'''
Day 9: Recursion
Task:
Write a factorial function that takes a positive integer,
N as a parameter and prints the result of N! (N factorial).

Explanation:
Consider the following steps:

1. factorial(3)= 3 x factorial(2)
2. factorial(2)= 2 x factorial(1)
3. factorial(1)= 1

From steps 2 and 3, we can say factorial(2) = 2 * 1 = 2;
then when we apply the value from factorial(2) to step 1,
we get factorial(3) = 3 * 2 * 1 = 6. Thus, we print 6 as our answer.
'''

#!/bin/python3

import sys


def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n - 1))


if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
