class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        def isprime(n):
            if n < 2: 
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        while left < right:
            isleft = isprime(nums[left])
            isright = isprime(nums[right])
            if isleft and isright:
                return abs(right - left)
            elif not isleft and isright:
                left = left + 1
            else:
                right = right - 1
        return 0
