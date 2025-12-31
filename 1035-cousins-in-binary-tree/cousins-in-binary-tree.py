# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def findDepth(node, parent, val, level):
            if not node:
                return None
            if node.val == val:
                return (level, parent)
            return findDepth(node.left, node, val, level + 1) or findDepth(node.right, node, val, level + 1)

        xdepth, xparent = findDepth(root, None, x, 0)
        ydpeth, yparent = findDepth(root, None, y, 0)
        return xdepth == ydpeth and xparent != yparent
