class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixmap = {}

        for num in arr1:
            strnum = str(num)
            prefix = ""
            for ch in strnum:
                prefix += ch
                prefixmap[prefix] = prefixmap.get(prefix, 0) + 1

        max_len = 0
        for num in arr2:
            strnum = str(num)
            prefix = ""
            for ch in strnum:
                prefix += ch
                if prefix in prefixmap:
                    max_len = max(max_len, len(prefix))
        return max_len
