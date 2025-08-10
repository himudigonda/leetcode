class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # # BruteForce
        # def _is_subsequence(word, s):
        #     s_ptr = 0
        #     w_ptr = 0

        #     while s_ptr < len(s) and w_ptr < len(word):
        #         if s[s_ptr] == word[w_ptr]:
        #             w_ptr += 1
        #         s_ptr += 1
        #     return w_ptr == len(word)

        # count = 0
        # for word in words:
        #     if _is_subsequence(word, s):
        #         count += 1
        # return count

        # # Optimal
        # waitingWords = defaultdict(deque)
        # for word in words:
        #     waitingWords[word[0]].append((word, 0))

        # matchCount = 0

        # for char in s:
        #     for _ in range(len(waitingWords[char])):
        #         word, w_ptr = waitingWords[char].popleft()
        #         w_ptr += 1
        #         if w_ptr == len(word):
        #             matchCount += 1
        #         else:
        #             waitingWords[word[w_ptr]].append((word, w_ptr))
        # return matchCount

        # Optimal Simple
        matching = 0
        buckets = defaultdict(list)
        for word in words:
            buckets[word[0]].append(word)
        for ch in s:
            bucket = buckets[ch]
            buckets[ch] = []
            for word in bucket:
                if len(word) == 1:
                    matching += 1
                else:
                    buckets[word[1]].append(word[1:])
        return matching
