class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set1 = set(list1)
        set2 = set(list2)
        common = set1.intersection(set2)
        resnum = float("inf")
        res = []
        map1 = defaultdict(int)
        map2 = defaultdict(int)
        for idx, val in enumerate(list1):
            map1[val] = idx
        for idx, val in enumerate(list2):
            map2[val] = idx

        for i in common:
            l1 = map1[i]
            l2 = map2[i]
            summ = l1 + l2
            if summ < resnum:
                resnum = summ
                res = [i]
            elif summ == resnum:
                res.append(i)
        return res
