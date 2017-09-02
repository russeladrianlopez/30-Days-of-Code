'''
Day 0: Hello, World.
Task:
To complete this challenge, you must save a line of input from stdin to a
variable, print Hello, World. on a single line, and finally print the
value of your variable on a second line.

Print Hello, World. on the first line, and the contents of inputString
on the second line.

Explanation:
On the first line, we print the string literal Hello, World.. On the second
line, we print the contents of the inputString variable which, for this
sample case, happens to be Welcome to 30 Days of Code!. If you do not print
the variable's contents to stdout, you will not pass the hidden test case.
'''

# Read a full line of input from stdin and save it to our dynamically
# typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')

# TODO: Write a line of code here that prints the contents of input_string
# to stdout.
print(input_string)
