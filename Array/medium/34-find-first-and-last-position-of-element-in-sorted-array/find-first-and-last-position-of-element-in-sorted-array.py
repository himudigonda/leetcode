class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findfirst(firstorlast = 0):
            left = 0
            right = len(nums) - 1
            best = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    if firstorlast == 0:
                        best = mid
                        left = mid + 1
                    elif firstorlast == 1:
                        best = mid
                        right = mid - 1
            return best
        
        left = findfirst(1)
        if left == -1: return [-1, -1]
        right = findfirst(0)
        return [left, right]