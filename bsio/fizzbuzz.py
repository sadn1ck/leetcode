"""
Given an integer n, return a list of integers from 1 to n as strings 
except for multiples of 3 use “Fizz” instead of the integer 
and for the multiples of 5 use “Buzz”. 
For integers which are multiples of both 3 and 5 use “FizzBuzz”.


"""


class Solution:
    def solve(self, n):
        fb = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                fb.append("FizzBuzz")
            elif i % 3 == 0:
                fb.append("Fizz")
            elif i % 5 == 0:
                fb.append("Buzz")
            else:
                fb.append(str(i))
        return fb
