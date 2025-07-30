class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)

        latest = [-1] * 32

        for i in range(len(nums) - 1, -1, -1):
            farthest = i

            for bit in range(32):
                if (nums[i] >> bit) & 1:
                    latest[bit] = i
                if latest[bit] != -1:
                    farthest = max(farthest, latest[bit])
            answer[i] = farthest - i + 1
        return answer
