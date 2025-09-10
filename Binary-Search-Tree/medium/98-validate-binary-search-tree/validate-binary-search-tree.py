# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # pass the ranges for each next recursive node.
        # update the range according to the values
        # and then call the next node with the updated range.
        def isValid(left, node, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return (isValid(left, node.left, node.val) and 
                    isValid(node.val, node.right, right))

        return isValid(float("-inf"), root, float("inf"))