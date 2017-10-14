'''
Day 21: Generics
Task:
Write a single generic function named printArray; this function must take an
array of generic elements as a parameter (the exception to this is C++, which
takes a vector). The locked Solution class in your editor tests your function.

Note: You must use generics to solve this challenge. Do not write overloaded
functions.

Input Format:
The locked Solution class in your editor will pass different types of arrays
to your printArray function.

Constraints:
You must have exactly 1 function named printArray.

Output Format:
Your printArray function should print each element of its generic array
parameter on a new line.
'''

# This is not an issue with Python since python list can basically handle all
# kinds of data type. Here is an example:


def printArray(arr):
    for i in arr:
        print(i)


intArray = [1, 20, 300, -50, 2.5]
stringArray = ["string", "Array"]
tupleArray = [("tuple", "Array")]
combineArray = [1, "Program", ("to", "rule", "them", "all")]

printArray(intArray)
printArray(stringArray)
printArray(tupleArray)
printArray(combineArray)
