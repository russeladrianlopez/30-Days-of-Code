'''
Day 11: 2D Array
Task:
Calculate the hourglass sum for every hourglass in A,
then print the maximum hourglass sum.


Sample Input:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output:
19

Explanation:
A contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

The hourglass with the maximum sum (19) is:
2 4 4
  2
1 2 4
'''

#!/bin/python3

import sys


arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

# Since every value ranges from -9 to 9
# lowest possible value is 7 * (-9)
largest = 7 * (-9)

for i in range(4):
    for j in range(4):
        t1, t2, t3 = arr[i][j], arr[i][j + 1], arr[i][j + 2]
        m2 = arr[i + 1][j + 1]
        b1, b2, b3 = arr[i + 2][j], arr[i + 2][j + 1], arr[i + 2][j + 2]

        value = t1 + t2 + t3 + m2 + b1 + b2 + b3
        largest = max(largest, value)

print(largest)
