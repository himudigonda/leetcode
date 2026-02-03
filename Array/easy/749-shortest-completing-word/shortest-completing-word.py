class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate = "".join([i.lower() for i in licensePlate if i.isalpha()])

        words = sorted(words, key=len)
        for word in words:
            freq = Counter(word)
            for i in range(len(plate)):
                if freq[plate[i]] < plate.count(plate[i]):
                    break
                if i == len(plate) - 1:
                    return word
