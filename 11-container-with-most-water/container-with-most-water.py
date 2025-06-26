class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            maxarea = max(area, maxarea)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxarea
