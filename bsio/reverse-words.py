"""
Given a string of words delimited by spaces, reverse the order of words. For example, given "hello there my friend", return "friend my there hello".


"""

class Solution:
    def solve(self, sentence):
        return ' '.join(list(sentence.split())[::-1])
