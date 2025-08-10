# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        prev = None
        maxcount = 0
        curcount = 0
        result = []

        def dfs(node):
            if not node:
                return
            nonlocal prev
            nonlocal maxcount
            nonlocal curcount
            nonlocal result

            dfs(node.left)
            curcount = 1 if node.val != prev else curcount + 1
            if curcount == maxcount:
                result.append(node.val)
            elif curcount > maxcount:
                result = [node.val]
                maxcount = curcount
            prev = node.val
            dfs(node.right)

        dfs(root)
        return result
