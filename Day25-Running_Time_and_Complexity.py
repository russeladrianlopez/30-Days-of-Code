'''
Day 25: Running Time and Complexity
Task:
A prime is a natural number greater than 1 that has no positive divisors
other than 1 and itself. Given a number, n, determine and print whether
it's Prime or Not prime.

Note: If possible, try to come up with a O(sqrt(n)) primality algorithm,
or see what sort of optimizations you come up with for an O(n) algorithm.
Be sure to check out the Editorial after submitting your code!

Sample Input:
3
12
5
7

Sample Output:
Not prime
Prime
Prime
'''

from math import sqrt

T = int(input())


def isPrime(n):
    sq = int(sqrt(n)) + 1
    for i in range(2, sq):
        if n % i == 0:
            return False
    return True


for i in range(T):
    n = int(input())
    if n > 1 and isPrime(n):
        print("Prime")
    else:
        print("Not prime")
