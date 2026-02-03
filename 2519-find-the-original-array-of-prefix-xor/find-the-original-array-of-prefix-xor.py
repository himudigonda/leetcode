class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # prev = pref[0]
        # for cur in range(1, len(pref)):
        #     pref[cur] ^= prev
        #     prev ^= pref[cur]

        # return pref

        prev = pref[0]
        ans = [pref[0]]

        for cur in pref[1:]:
            ans.append(prev ^ cur)
            prev = cur
        return ans
