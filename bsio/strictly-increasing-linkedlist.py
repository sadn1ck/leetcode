"""
Given the head of a singly linked list head, return whether the values of the nodes are sorted in a strictly ascending order.


"""

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def solve(self, head):
        while head.next is not None:
            if head.next.val <= head.val:
                return False
            head = head.next
        return True
