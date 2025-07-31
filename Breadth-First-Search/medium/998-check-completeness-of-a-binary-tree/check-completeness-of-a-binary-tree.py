# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # BruteForce
        nullseen = False

        queue = deque([root])
        while queue:
            if nullseen:
                return not any(queue)
            else:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if not node:
                        nullseen = True
                    else:
                        if nullseen:
                            return False
                        else:
                            queue.append(node.left)
                            queue.append(node.right)
        return True
