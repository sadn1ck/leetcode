"""

You are given a binary tree root with each node containing single digits from 0 to 9. Each path from the root to the leaf represents a number with its digits in order.

Return the sum of numbers represented by all paths in the tree.

For example, given the following tree:

   3
  / \
 5   2
    / \
   1   4
we have the following numbers represented by paths:

35 (3 → 5)
321 (3 → 2 → 1)
324 (3 → 2 → 4)
and their sum is 680.
"""

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root):
        def dfs(node, v=0):
            if node:
                v = 10 * v + node.val
                if node.left is node.right is None:
                    self.ans += v
                dfs(node.left, v)
                dfs(node.right, v)

        self.ans = 0
        dfs(root)
        return self.ans
