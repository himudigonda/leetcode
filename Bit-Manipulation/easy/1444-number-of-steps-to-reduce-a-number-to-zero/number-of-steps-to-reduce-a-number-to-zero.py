class Solution:
    def numberOfSteps(self, num: int) -> int:
        # # BruteForce
        # steps = 0
        # while num != 0:
        #     steps += 1
        #     if num & 1:
        #         num -= 1
        #     else:
        #         num >>= 1
        # return steps

        # Optimal
        if num == 0:
            return 0
        return num.bit_length() - 1 + num.bit_count()
