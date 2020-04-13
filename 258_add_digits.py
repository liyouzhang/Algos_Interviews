'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

'''

# 2020.04.13 Yay! I coded it myself :)

class Solution:
    def addDigits(self, num: int) -> int:
        # cast the int into string, and split it into a list of sigal digit int
        # while loop if the output is not <10 and >0 
        # then add on the digit 
        output = self.calculate(num)
        while output >= 10:
            output = self.calculate(output)
        return output 

    def calculate(self, num: int) -> int:
    # def calculate(num):
        output = 0 
        s = str(num)
        for i in s:
            output += int(i)
        return output 
