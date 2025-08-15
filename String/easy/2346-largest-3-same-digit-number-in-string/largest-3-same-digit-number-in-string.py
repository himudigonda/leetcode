class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ## BruteForce
        # best = ""
        # for i in range(len(num) - 2):
        #     if num[i] == num[i+1] == num[i+2]:
        #         best = max(best, num[i:i+3])
        # return best

        # Optimal
        lennums = []
        for i in range(0, 10):
            temp = 3 * str(i)
            lennums.append(temp)

        for i in lennums[::-1]:
            if i in num:
                return i
        return ""

        # OneLiner
        # return max((x*3 for x,y,z in zip(num, num[1:], num[2:]) if x==y==z), default='')
