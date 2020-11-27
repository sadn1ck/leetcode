"""
Given a singly linked list node, return its reverse. For example, given 1 -> 2 -> 3 -> 4, return 4 -> 3 -> 2 -> 1.

You should return the head of the reversed list, so in this case the node containing the 4.

Bonus: Can you do this in O(1) space?


"""

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def solve(self, node):
        curr, prev, nxt = node, None, None
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
