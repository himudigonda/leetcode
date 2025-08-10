class Solution:
    def intToRoman(self, num: int) -> str:
        # # BruteForce
        # ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        # tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        # hrns = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        # ths = ["", "M", "MM", "MMM"]

        # return (
        #     ths[num // 1000]
        #     + hrns[(num % 1000) // 100]
        #     + tens[(num % 100) // 10]
        #     + ones[num % 10]
        # )

        # Optimal
        value2sym = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        res = []
        for val, sym in value2sym:
            if num // val:
                count = num // val
                res.append(sym * count)
                num = num % val
        return "".join(res)
