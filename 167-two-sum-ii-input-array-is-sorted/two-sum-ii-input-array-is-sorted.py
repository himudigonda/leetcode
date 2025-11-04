class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # # Bruteforce
        # for i in range(len(numbers)):
        #     for j in range(len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        # return [-1,-1]
        
        # # since the input is sorted we can use 2 points
        # left = 0
        # right = len(numbers) - 1
        # while left < right:
        #     cur =  numbers[left] + numbers[right]
        #     if cur == target:
        #         return [left + 1, right + 1]
        #     elif cur < target:
        #         left += 1
        #     else:
        #         right -= 1
        # return [-1, -1]

        # Binary search approach
        for i in range(len(numbers)):
            complement = target - numbers[i]
            l, r = i + 1, len(numbers) - 1
            while l <= r:
                m = (l + r) // 2
                if numbers[m] == complement:
                    return [i + 1, m + 1]
                elif numbers[m] < complement:
                    l = m + 1
                else:
                    r = m - 1
        return [-1, -1]