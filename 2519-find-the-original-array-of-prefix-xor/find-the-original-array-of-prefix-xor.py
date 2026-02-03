class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        prev = pref[0]
        for cur in range(1, len(pref)):
            pref[cur] ^= prev
            prev ^= pref[cur]

        return pref
