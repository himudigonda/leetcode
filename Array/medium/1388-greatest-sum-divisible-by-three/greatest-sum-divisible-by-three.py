class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = 0
        smallestOne = float('inf')
        smallestTwo = float('inf')
        for n in nums:
            total += n
            if n % 3 == 1:
                smallestTwo = min(smallestTwo, smallestOne + n)
                smallestOne = min(smallestOne, n)
            if n % 3 == 2:
                smallestOne = min(smallestOne, smallestTwo + n)
                smallestTwo = min(smallestTwo, n)

        
        if total % 3 == 0: return total
        if total % 3 == 1: return total - smallestOne
        if total % 3 == 2: return total - smallestTwo