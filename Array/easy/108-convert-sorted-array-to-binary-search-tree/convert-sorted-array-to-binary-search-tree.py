# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # # Pass arr as args to self recursion
        # if not nums:
        #     return None

        # mid = len(nums) // 2
        # root = TreeNode(nums[mid])
        # root.left = self.sortedArrayToBST(nums[:mid])
        # root.right = self.sortedArrayToBST(nums[mid + 1 :])
        # return root

        # helper function based recursion with left and right
        def sortitup(left, right):
            if left > right:
                return

            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = sortitup(left, mid - 1)
            node.right = sortitup(mid + 1, right)
            return node

        return sortitup(0, len(nums) - 1)
