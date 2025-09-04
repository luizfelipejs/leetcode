import math

# For two strings s and t, 
# we say "t divides s" if and only if s = t + t + t + ... + t + t 
# (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, 
# return the largest string x such that x divides both str1 and str2.

 
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def mdc(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a
        
        
        if str1 + str2 != str2 + str1:
            return ""
        
        
        tam = mdc(len(str1), len(str2))
        
        
        return str1[:tam]