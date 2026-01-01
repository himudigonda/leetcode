# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def getDepth(node, left):
            d = 0
            while node:
                node = node.left if left else node.right
                d += 1
            return d

        right = getDepth(root.left, True) + 1
        left = getDepth(root.right, False) + 1
        if right == left:
            return (1 << right) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
