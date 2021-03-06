# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/broken-calculator/

#1 Brute force, BFS from X to Y => TLE. 

#2 From Y to X. 
If Y % 2 == 0, Y //= 2.
If Y % 2 !=0, Y += 1.
Reason:
If Y is even, (Y + 2) // 2 VS Y // 2 + 1, the 2nd uses less operations. 
If Y is odd, (Y + 3) // 2 VS (Y + 1) // 2 + 1, the 2nd uses less operations. 
"""
class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        if X == Y:
            return 0
        
        if X > Y:
            return X - Y
        
        if (Y % 2 == 1):
            return 1 + self.brokenCalc(X, Y + 1)
        else:
            return 1 + self.brokenCalc(X, Y // 2)
