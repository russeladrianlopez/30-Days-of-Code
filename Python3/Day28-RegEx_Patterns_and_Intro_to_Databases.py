'''
Day 28: RegEx, Patterns, and Intro to Databases
Task:
Consider a database table, Emails, which has the attributes First Name
and Email ID. Given N rows of data simulating the Emails table, print
an alphabetically-ordered list of people whose email address ends in
@gmail.com.

Print an alphabetically-ordered list of first names for every user with
a gmail account. Each name must be printed on a new line.

Sample Input:
6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com

Sample Output:
julia
julia
riya
samantha
tanya
'''

#!/bin/python3

import sys
import re


N = int(input().strip())
gmail_accounts = []
for a0 in range(N):
    firstName, emailID = str(input()).strip().split(' ')

    if re.search("^[a-z\.]+@gmail.com$", emailID):
        gmail_accounts.append(firstName)

gmail_accounts.sort()
for n in gmail_accounts:
    print(n)
