class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maxnum = float('inf')
        for i in nums:
            if i == maxnum:
                count += 1
            else:
                if count == 0:
                    maxnum = i
                    count = 1
                else:
                    count -= 1
        return maxnum