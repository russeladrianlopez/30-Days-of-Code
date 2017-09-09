'''
Day 8: Dictionaries and Maps
Task:
Given n names and phone numbers, assemble a phone book that maps
friends' names to their respective phone numbers. You will then be given
an unknown number of names to query your phone book for. For each name
queried, print the associated entry from your phone book on a new line in
the form name=phoneNumber; if an entry for name is not found, print Not
found instead.

Note:
- Your phone book should be a Dictionary/Map/HashMap data structure.
- Names consist of lowercase English alphabetic letters and are first
names only.

On a new line for each query, print Not found if the name has no
corresponding entry in the phone book; otherwise, print the full name
and phoneNumber in the format name=phoneNumber.

Sample Input:
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Sample Output:
sam=99912222
Not found
harry=12299933
'''

n = int(input())

phone_book = {}

for i in range(0, n):
    entry = str(input()).split(" ")

    name = entry[0]
    phone = int(entry[1])
    phone_book[name] = phone

for x in range(0, n):
    name = str(input())

    if name in phone_book:
        phone = phone_book[name]
        print("{}={}".format(name, phone))
    else:
        print("Not found")
