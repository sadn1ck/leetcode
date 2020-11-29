"""
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure incidate the result:


"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start, end = None, None
        end = list1
        while end.val != b:
            end = end.next
        # print(end)
        start = list1
        while start.next.val != a:
            start = start.next
        start.next = list2
        while start.next is not None:
            start = start.next
        start.next = end.next
        return list1
