class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        # player1 = 0
        # player2 = 0
        # player1flag = True
        # player2flag = False

        # for idx, val in enumerate(nums):
        #     if idx % 6 == 5:
        #         player1flag = not player1flag
        #         player2flag = not player2flag
        #     if val % 2 == 1:
        #         player1flag = not player1flag
        #         player2flag = not player2flag
        #     player1 += val if player1flag else 0
        #     player2 += val if player2flag else 0
        # return player1 - player2

        scores = [0, 0]
        active = True

        for idx, val in enumerate(nums):
            if val % 2:
                active = not active
            if idx % 6 == 5:
                active = not active

            if active:
                scores[0] += val
            else:
                scores[1] += val

        return scores[0] - scores[1]
