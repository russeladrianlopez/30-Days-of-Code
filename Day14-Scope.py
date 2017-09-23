'''
Day 14: Scope
Task
Complete the Difference class by writing the following:

- A class constructor that takes an array of integers as a parameter and saves
it to the elements instance variable.
- A computeDifference method that finds the maximum absolute difference between
any 2 numbers in N and stores it in the maximumDifference instance variable.

Sample Input:
3
1 2 5

Sample Output:
4

Explanation:
The scope of the elements array and maximumDifference integer is the entire
class instance. The class constructor saves the argument passed to the
constructor as the elements instance variable (where the computeDifference
method can access it).

To find the maximum difference, computeDifference checks each element in the
array and finds the maximum difference between any 2 elements:
|1 - 2| = 1
|1 - 5| = 4
|2 - 5| = 3

The maximum of these differences is 4, so it saves the value 4 as the
maximumDifference instance variable. The locked stub code in the editor then
prints the value stored as maximumDifference, which is 4.
'''


class Difference:

    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        self.maximumDifference = 0

        dupelist = []  # duplicate checker
        for i in self.__elements:
            for j in self.__elements:
                if [i, j] and [j, i] not in dupelist and (i != j):
                    value = abs(i - j)
                    dupelist.append([i, j])
                    self.maximumDifference = max(self.maximumDifference, value)


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
