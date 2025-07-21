class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ## BruteForce
        # result = set()
        # strint = [str(i) for i in range(0, 10)]

        # def bt(i, curstr):
        #     if i == len(s):
        #         result.add(curstr)
        #         return
        #     if s[i] in strint:
        #         bt(i + 1, curstr + s[i])
        #     else:
        #         bt(i + 1, curstr + s[i].lower())
        #         bt(i + 1, curstr + s[i].upper())

        # bt(0, "")
        # return list(result)

        # Optimal
        results = [""]
        for char in s:
            if char.isalpha():
                results = [
                    prefix + c
                    for prefix in results
                    for c in (char.lower(), char.upper())
                ]
            else:
                results = [prefix + char for prefix in results]
        return results
