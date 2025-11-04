class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # bruteforce
        # n = len(nums)
        # res = [1] * n
        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i != j: prod *= nums[j]
        #     res[i] = prod
        # return res

        # # prefix suffix: arr -> O(n) & O(n)
        # n = len(nums)
        # prefix = [1] * n
        # suffix = [1] * n
        # res = [1] * n

        # for i in range(1, n):
        #     prefix[i] = prefix[i - 1] * nums[i - 1]
        # for i in range(n-2, -1, -1):
        #     suffix[i] = suffix[i + 1] * nums[i + 1]
        # for i in range(n):
        #     res[i] = prefix[i] * suffix[i]
        # return res

        # prefix suffix : int -> O(2*n) & O(1): 2 pass solution
        n = len(nums)
        prefix = 1
        suffix = 1
        res = [1] * n
        for i in range(n):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        for j in range(n - 1, -1, -1):
            res[j] = res[j] * suffix
            suffix = suffix * nums[j]
        return res