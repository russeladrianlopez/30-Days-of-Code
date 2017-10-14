'''
Day 27: Testing
Problem Statement:
A Discrete Mathematics professor has a class of n students. Frustrated with
their lack of discipline, the professor decides to cancel class if fewer than
k students are present when class starts. Given the arrival time of each
student, determine if the class is canceled.

Input Format:
The first line of input contains t, the number of lectures.
The information for each lecture spans two lines. The first line has two
space-separated integers, n (the number of students in the class) and k (the
cancelation threshold). The second line contains n space-separated integers
describing the array of students' arrival times (A= a(i0), a(i1), ..., a(i-1)).

Note: Non-positive arrival times (a(i) < 0) indicate the student arrived early
or on time; positive arrival times (a(i) > 0) indicate the student arrived a(i)
minutes late. If a student arrives exactly on time , the student is considered
to have entered before the class started.

Output Format:
For each test case, print the word YES if the class is canceled or NO if it
is not.

Task:
Task

Create and print a test case for the problem above that meet the following
criteria:

- t <= 5
- 3 <= n <= 200
- 1 <= k <= n
- -10^3 <= a(i) <= 10^3
- Array must have atleast 1 zero, 1 positive integer and 1 negative integer.

The value of  must be distinct across all the test cases.
Array  must have at least  zero,  positive integer, and  negative integer.
Scoring

If you submit x correct test cases, you will earn (20*x)% of the maximum score.
You must submit 5 test cases to earn the maximum possible score.
'''

from random import randint

T = randint(5, 15)
print(T)
for t in range(T):
    n = 3 + t
    k = randint(1, n)
    arr = [-1, 0, 1]
    for i in range(n - 3):
        arr.append(randint(-1000, 1000))

    print(n, k)
    print(*arr, sep=" ")
