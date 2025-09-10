class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first), len(last))):
            print(first, last)
            if first[i] == last[i]:
                ans.append(first[i])
            else:
                return "".join(ans)
        return "".join(ans)
