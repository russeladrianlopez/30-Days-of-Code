'''
Day 7: Arrays
Task:
Given an array, A, of N integers, print A's elements in reverse
order as a single line of space-separated numbers.

Print the elements of array A in reverse order as a single line
of space-separated numbers.

Sample Input:
4
1 4 3 2

Sample Output:
2 3 4 1
'''
#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

# arr = arr[::-1] or
arr.reverse()

print(" ".join(str(x) for x in arr))
