class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        length = len(words)
        concat = "".join(words)
        counts = {}

        if len(concat) % length != 0:
            return False

        for ch in concat:
            counts[ch] = counts.get(ch, 0) + 1

        for val in counts.values():
            if val % length != 0:
                return False
        return True
