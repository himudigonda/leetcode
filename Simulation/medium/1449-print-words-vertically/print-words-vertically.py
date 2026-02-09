class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        maxlen = max(len(word) for word in words)
        ans = []

        for i in range(maxlen):
            cur = ""
            for word in words:
                cur += word[i] if i < len(word) else " "
            ans.append(cur.rstrip())
        return ans
        #     l = []
        #     for word in words:
        #         l.append(word[i] if i < len(word) else " ")
        #     ans.append("".join(l).rstrip())
        # return ans
