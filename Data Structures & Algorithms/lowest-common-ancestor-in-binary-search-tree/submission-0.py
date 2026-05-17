# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        a, b = sorted((p.val, q.val))  # ensure a <= b
        node = root
        while node:
            if b < node.val:
                node = node.left         # both on the left
            elif a > node.val:
                node = node.right        # both on the right
            else:
                return node              # split here (or one equals node)
        return None