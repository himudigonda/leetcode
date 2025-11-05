class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) == 0: return 0
        if len(colors) == 1: return 0
        left = 0
        count = 0
        for right in range(1, len(colors)):
            if colors[left]  == colors[right]:
                if neededTime[left] < neededTime[right]:
                    count += neededTime[left]
                    left = right
                else:
                    count += neededTime[right]
            else:
                left = right
        return count

