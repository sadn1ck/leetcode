/*
 * Given two binary strings, return their sum (also a binary string).
 *
 * The input strings are both non-empty and contains only characters 1 or 0.
 */

class Solution:
	    def addBinary(self, a: str, b: str) -> str:
	            x = int(a, 2)
	            y = int(b, 2)
	            s = x + y
	            print(x,y,s)
	            t = str(bin(s))
	            return t[2:]
