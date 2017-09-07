'''
Day 6: Let's Review
Task:
Given a string, S, of length N that is indexed from 0 to N-1, print
its even-indexed and odd-indexed characters as 2 space-separated strings
 on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Sample Input:
2
Hacker
Rank

Sample Output:
Hce akr
Rn ak
'''

n = int(input())

for x in range(0, n):
    even, odd = "", ""
    s = input()

    for i in range(0, len(s)):
        if i % 2 == 0:
            even += s[i]
        else:
            odd += s[i]

    print("{} {}".format(even, odd))
