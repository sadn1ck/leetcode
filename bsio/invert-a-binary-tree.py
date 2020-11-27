"""
Given a binary tree root, invert it so that its left subtree and right subtree are swapped and the children are recursively inverted.

For example, given

  0
 / \
2   9
   / \
  7   12
Return

    0
   / \
  9   2
 / \
12   7

"""

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Yes this is my solution, how trash right?
# I agree, this is trash LOL

class Solution:
    def solve(self, root):
        def invert(node):
            if node:
                if node.left is None and node.right is None:
                    return
                elif node.left is None and node.right is not None:
                    node.left = node.right
                    node.right = None
                    invert(node.left)
                elif node.right is None and node.left is not None:
                    node.right = node.left
                    node.left = None
                    invert(node.right)
                else:
                    node.left, node.right = node.right, node.left
                    invert(node.left)
                    invert(node.right)
        invert(root)
        return root

class Editorial:
    def solve(self, root):
        if root:
            root.right, root.left = self.solve(root.left), self.solve(root.right)
        return root