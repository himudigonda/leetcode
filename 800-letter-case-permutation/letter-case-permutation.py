class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = set()
        strint = [str(i) for i in range(0, 9)]

        def bt(i, curstr):
            if i == len(s):
                result.add(curstr)
                return
            if s[i] in strint:
                bt(i + 1, curstr + s[i])
            else:
                bt(i + 1, curstr + s[i].lower())
                bt(i + 1, curstr + s[i].upper())

        bt(0, "")
        return list(result)
