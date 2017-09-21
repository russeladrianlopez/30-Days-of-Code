'''
Day 12: Inheritance
Task:
You are given two classes, Person and Student, where Person is the base class
and Student is the derived class. Completed code for Person and a declaration
for Student are provided for you in the editor. Observe that Student inherits
all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has 4 parameters:
A string, firstName.
A string, lastName.
An integer, id.
An integer array (or vector) of test scores, scorces.
A char calculate() method that calculates a Student object's average and
returns the grade character representative of their calculated average:

Grading Scale:
O = 90 or more
E = 80 to 90
A = 70 to 80
P = 55 to 70
D = 40 to 55
T = less than 40


This is handled by the locked stub code in your editor. Your output will be
correct if your Student class constructor and calculate() method are properly
implemented.

Sample Input:
Heraldo Memelli 8135627
2
100 80

Sample Output:
Name: Memelli, Heraldo
ID: 8135627
Grade: O

Explanation:
This student had 2 scores to average: 100 and 80. The student's average grade
is (100+80)/2 = 90. An average grade of 90 corresponds to the letter grade O,
so our calculate() method should return the character'O'.
'''


class Person:

    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avg = sum(self.scores) / len(self.scores)

        if avg >= 90:
            return "O"
        elif avg >= 80 and avg < 90:
            return "E"
        elif avg >= 70 and avg < 80:
            return "A"
        elif avg >= 55 and avg < 70:
            return "P"
        elif avg >= 40 and avg < 55:
            return "D"
        return "T"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
