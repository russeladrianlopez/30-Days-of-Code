'''
Day 29: Bitwise AND
Task:
Given set S = {1,2,3,...,N}. Find two integers, A and B (where A < B), from
set S such that the value of A&B is the maximum possible and also less than
a given integer, K. In this case, & represents the bitwise AND operator.

Input Format:
The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines defines a test case as 2 space-separated
integers, N and K, respectively.

Output Format:
For each test case, print the maximum possible value of  on a new line.

Sample Input:
3
5 2
8 5
2 2

Sample Output:
1
4
0

'''

# Initial Answer
# (Upon Submission Timeout Error Occurs for the more complicated Test Cases)
# #!/bin/python3

# import sys


# t = int(input().strip())
# for a0 in range(t):
#     n, k = map(int, input().strip().split(' '))

#     maximum = 0

#     for i in range(1, n):
#         for j in range(i + 1, n + 1):
#             if i & j < k:
#                 maximum = max(maximum, i & j)

# print(maximum)


# Time Efficient Answer (But does not use the & operator instead uses | ).
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n, k = map(int, input().strip().split(' '))

    if ((k - 1) | k) <= n:
        print(k - 1)
    else:
        print(k - 2)
