# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # # DFS
        # if not root:
        #     return 0

        # if not root.left and not root.right:
        #     return 1

        # min_depth = float("inf")

        # if root.left:
        #     min_depth = min(min_depth, self.minDepth(root.left))
        # if root.right:
        #     min_depth = min(min_depth, self.minDepth(root.right))

        # return 1 + min_depth

        # BFS
        if not root:
            return 0
        q = deque([(root, 1)])

        while q:
            node, depth = q.popleft()
            if not node.left and not node.right:
                return depth

            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
