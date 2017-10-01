'''
Day 26: Nested Logic
Task:
Your local library needs your help! Given the expected and actual return
dates for a library book, create a program that calculates the fine (if any).
The fee structure is as follows:

1. If the book is returned on or before the expected return date, no fine will
be charged (i.e.: fine = 0).

2. If the book is returned after the expected return day but still within the
same calendar month and year as the expected return date, fine = 15 Hackos x
(the number of day late).

3. If the book is returned after the expected return month but still within the
same calendar year as the expected return date, the fine = 500 Hackos x (the
number of months late).

4. If the book is returned after the calendar year in which it was expected,
there is a fixed fine of 10000 Hackos.

Sample Input:
9 6 2015
6 6 2015

Sample Output:
45
'''


from datetime import date

a = list(map(int, input().strip().split(' ')))
e = list(map(int, input().strip().split(' ')))

actual = date(day=a[0], month=a[1], year=a[2])
expected = date(day=e[0], month=e[1], year=e[2])

fine = 0

if actual > expected:
    if actual.year == expected.year:
        if actual.month == expected.month:
            fine = 15 * (actual.day - expected.day)
        else:
            fine = 500 * (actual.month - expected.month)
    else:
        fine = 10000

print(fine)
