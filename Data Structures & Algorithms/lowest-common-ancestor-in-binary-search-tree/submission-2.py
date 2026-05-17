# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        a, b = sorted((p.val, q.val))
        node = root

        while node:

            if a <= node.val <= b:
                return node
            elif a < node.val and b < node.val:
                node = node.left
            else:
                node = node.right
        
        