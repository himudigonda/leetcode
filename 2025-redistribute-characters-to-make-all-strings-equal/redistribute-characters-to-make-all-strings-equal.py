class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = {}
        length = len(words)

        for word in words:
            for ch in word:
                counts[ch] = counts.get(ch, 0) + 1

        for val in counts.values():
            if val % length != 0:
                return False
        return True