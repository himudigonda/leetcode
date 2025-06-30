class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        for i in c.keys():
            if c[i] == 1:
                k -= 1
                if k == 0:
                    return i
        return ""