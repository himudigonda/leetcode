from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Hashmap approach
        return Counter(s) == Counter(t)

        # # Manual Hashmap(arr-26letters) freq map
        # if len(s) != len(t): return False

        # counts = [0] * 26

        # for i in range(len(s)):
        #     counts[ord(s[i]) - ord('a')] += 1
        #     counts[ord(t[i]) - ord('a')] -= 1
        # return all(c == 0 for c in counts)

        # # Sorted comparision
        # return sorted(s) == sorted(t)