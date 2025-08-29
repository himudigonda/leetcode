# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # Brute Force
        # def dfs(node, depth):
        #     if not node:
        #         return 0
        #     depth += max(dfs(node.left, depth), dfs(node.right, depth))
        #     return depth

        # return dfs(root, 1)

        # Optimal
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
