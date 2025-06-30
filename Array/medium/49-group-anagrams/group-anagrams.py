class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)
        for s in strs:
            sorteds = sorted(s)
            mapp["".join(sorteds)].append(s)
        res = []
        for i in mapp.values():
            res.append(i)
        return res