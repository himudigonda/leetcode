from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # sort and map the word to their sorted version
        # mapps = defaultdict(list)
        # for word in strs:
        #     sorted_word = sorted(word)
        #     sorted_word = ''.join(sorted_word)
        #     mapps[sorted_word].append(word)
        # return list(mapps.values())

        # use character mapping instead of sorting.
        mapps = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            mapps[tuple(freq)].append(word)
        return list(mapps.values())