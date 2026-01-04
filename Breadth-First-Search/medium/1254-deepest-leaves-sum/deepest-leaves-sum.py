# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # # DFS
        # mapping = defaultdict(int)
        # maxdepth = 0

        # def dfs(node, depth):
        #     nonlocal maxdepth
        #     if not node: return

        #     maxdepth = max(maxdepth, depth)
        #     mapping[depth] += node.val
        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)
        #     return

        # dfs(root, 0)
        # return mapping[maxdepth]

        # BFS
        q = deque([root])

        while q:
            level_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not q:
                return level_sum
