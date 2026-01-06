# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])

        curlevel = 0
        level_num = 0
        maxsum = float("-inf")
        while q:
            curlevel += 1
            lenq = len(q)
            cursum = 0
            for _ in range(lenq):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                cursum += node.val
            if cursum > maxsum:
                maxsum = cursum
                level_num = curlevel
        return level_num
