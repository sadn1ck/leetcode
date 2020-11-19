"""
Given a binary tree containing integer vals, return the sum of all values in the tree.

For example, in this tree the sum is 10 = 0 + 1 + 2 + 1 + 0 + 3 + 3

   0
  / \
 1   2
    / \
   1   0
  / \
 3   3
"""

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root):
        def dfs(node):
            if node is not None:
                sm = node.val
                if node.left is not None:
                    sm += dfs(node.left)
                if node.right is not None:
                    sm += dfs(node.right)
                return sm
        if root is None:
            return 0
        return dfs(root)
