# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        from collections import deque, defaultdict

        queue = deque([(root, 1)])
        res = defaultdict(list)

        while queue:

            node, level = queue.popleft()

            if node:
                res[level].append(node.val)
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))

        return list(res.values())
        