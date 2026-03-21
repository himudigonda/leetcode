class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        mapping = []
        for num in arr:
            x = bin(num)[2:]
            counts = x.count("1")
            # counts = 0
            # for i in cur:
            #     if i == "1":
            #         counts += 1
            mapping.append((num, counts))

        temp = sorted(mapping, key=lambda x: (x[1], x[0]))
        return [i for i, j in temp]
        # return sorted(arr, key=lambda x: (bin(x).count('1'), x))
