# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        counts = defaultdict(int)
        if not root:
            return []

        def dfs(node):
            if not node:
                return 0
            leftval = dfs(node.left)
            rightval = dfs(node.right)
            summ = node.val + rightval + leftval
            counts[summ] += 1
            return summ

        dfs(root)
        maxfreq = max(counts.values())
        return [c for c in counts if counts[c] == maxfreq]
