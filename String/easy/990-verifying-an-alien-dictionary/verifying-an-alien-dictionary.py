class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {order[i]: i for i in range(len(order))}
        for i in range(1, len(words)):
            wordA, wordB = words[i - 1], words[i]
            for idxA in range(len(wordA)):
                if idxA == len(wordB):
                    return False
                aChar, bChar = wordA[idxA], wordB[idxA]
                aix, bix = mapping[aChar], mapping[bChar]
                if aix < bix:
                    break
                if aix > bix:
                    return False
        return True
