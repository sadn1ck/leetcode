"""
Given a string s, eliminate consecutive duplicate characters from the string and return it.

That is, if a list contains repeated characters, they should be replaced with a single copy of the character. 

The order of the elements should not be changed.
"""


class Solution:
    def solve(self, s):
        st = []
        for ch in s:
            if len(st) > 0:
                if st[-1] != ch:
                    st.append(ch)
            else:
                st.append(ch)
        return "".join(st)
