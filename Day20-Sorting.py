'''
Day 20: Sorting
Task:
Given an array, a, of size n distinct elements, sort the array in ascending
order using the Bubble Sort algorithm above. Once sorted, print the following
3 lines:

1. Array is sorted in numSwaps swaps.
where numSwaps is the number of swaps that took place.

2. First Element: firstElement
where firstElement is the first element in the sorted array.

3. Last Element: lastElement
where lastElement is the last element in the sorted array.

Hint: To complete this challenge, you will need to add a variable that keeps a
running tally of all swaps that occur during execution.

Sample Input 0:
3
1 2 3

Sample Output 0:
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3

Sample Input 1:
3
3 2 1

Sample Output 1:
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
'''

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# Write Your Code Here
swapcount = 0
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
            swapcount += 1

print("Array is sorted in {} swaps.".format(swapcount))
print("First Element: {}\nLast Element: {}".format(a[0], a[n - 1]))
