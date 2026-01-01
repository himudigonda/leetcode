class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])

        for word in words:
            curcount = Counter(word)
            for c in count:
                count[c] = min(count[c], curcount[c])

        res = []
        for c in count:
            # for i in range(count[c]):
            # res.append(c)
            res.extend([c] * count[c])
        return res
