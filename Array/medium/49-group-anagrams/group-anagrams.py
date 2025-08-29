class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            cString = "".join(sorted(string))
            result[cString].append(string)
        return list(result.values())
