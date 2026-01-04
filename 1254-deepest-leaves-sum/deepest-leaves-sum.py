# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        mapping = defaultdict(int)
        maxdepth = 0

        def dfs(node, depth):
            nonlocal maxdepth
            if not node: return
            
            maxdepth = max(maxdepth, depth)
            mapping[depth] += node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            return

        dfs(root, 0)
        return mapping[maxdepth]
