'''
Day 19: Interfaces
Task
The AdvancedArithmetic interface and the method declaration for the abstract
int divisorSum(int n) method are provided for you in the editor below. Write
the Calculator class, which implements the AdvancedArithmetic interface. The
implementation for the divisorSum method must be public and take an integer
parameter, n, and return the sum of all its divisors.

Sample Input:
6

Sample Output:
I implemented: AdvancedArithmetic
12

Explanation:
The integer 6 is evenly divisible by 1, 2, 3, and 6. Our divisorSum method
should return the sum of these numbers, which is 1 + 2 + 3 + 6 = 12.
The Solution class then prints "I implemented: AdvancedArithmetic" on the
first line, followed by the sum returned by divisorSum (which is 12) on
the second line.
'''

from abc import ABCMeta, abstractmethod


class AdvancedArithmetic(object, metaclass=ABCMeta):
    @abstractmethod
    def divisorSum(self, n):
        pass


class Calculator(AdvancedArithmetic):

    def divisorSum(self, n):
        result = 0
        for i in range(1, 1001):  # 1 <= n <= 1000 Contraints
            if n % i == 0:
                result += i
        return result


# n = int(input())
# No python3 version in HackerRank
n = 6  # sample input

calc = Calculator()
total = calc.divisorSum(n)
print("I implemented: Advanced Arithmetic\n{}".format(total))
