class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        # peak = arr.index(max(arr))

        # if peak == 0 or peak == n - 1:
        #     return False

        # for i in range(peak):
        #     if arr[i] >= arr[i + 1]:
        #         return False

        # for i in range(peak, n - 1):
        #     if arr[i] <= arr[i + 1]:
        #         return False

        # return True
        i = 0
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1
