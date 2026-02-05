class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold = threshold * k
        cursum = sum(arr[:k])
        count = 0

        if cursum >= threshold:
            count += 1

        for right in range(k, len(arr)):
            cursum = cursum - arr[right - k] + arr[right]
            if cursum >= threshold:
                count += 1
        return count
