"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: "Node") -> int:

        # def dfs(node):
        #     if not node:
        #         return 0
        #     res = [0]
        #     for child in node.children:
        #         res.append(dfs(child))
        #     return 1 + max(res)

        # return dfs(root)

        if not root:
            return 0

        q = deque([root])
        depth = 0

        while q:
            lenq = len(q)
            depth += 1
            for _ in range(lenq):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
        return depth
