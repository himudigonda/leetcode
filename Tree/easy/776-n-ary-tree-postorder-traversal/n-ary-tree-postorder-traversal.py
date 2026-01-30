"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        # res = []

        # def dfs(node):
        #     if not node:
        #         return
        #     for child in node.children:
        #         dfs(child)
        #     res.append(node.val)

        # dfs(root)
        # return res

        if not root:
            return []

        res = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))
                for child in node.children[::-1]:
                    stack.append((child, False))
        return res
