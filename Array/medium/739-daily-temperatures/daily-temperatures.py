class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                tem, ind = stack.pop()
                res[ind] = idx - ind
            stack.append([temp, idx])
        return res
