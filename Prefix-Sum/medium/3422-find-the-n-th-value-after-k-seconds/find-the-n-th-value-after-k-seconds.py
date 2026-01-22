class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        start = [1] * n
        iters = 0

        for iters in range(k):
            for i in range(1, len(start)):
                start[i] = start[i - 1] + start[i]

        return start[-1] % (10 ** 9 + 7)