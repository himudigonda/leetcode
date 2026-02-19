class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        # res = []
        # c = 1
        # while n > 0:
        #     num = n % 10
        #     if num > 0:
        #         res.append(num * c)
        #     n = n // 10
        #     c = c * 10
        # return res[::-1]

        s = str(n)
        res = []
        length = len(s)

        for i, char in enumerate(s):
            if char != "0":
                num = int(char) * (10 ** (length - 1 - i))
                res.append(num)
        return res
