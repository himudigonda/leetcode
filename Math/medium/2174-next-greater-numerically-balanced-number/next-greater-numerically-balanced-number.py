class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # Brute Force
        def is_balanced(num):
            # string = str(num)
            # counts = Counter(string)
            # for key, val in counts.items():
            #     if int(key) != val:
            #         return False
            # return True

            counts = [0] * 10
            temp = num
            while temp > 0:
                digit = temp % 10
                if digit == 0:
                    return False
                counts[digit] += 1
                temp //= 10
            for d in range(1, 10):
                if counts[d] > 0 and counts[d] != d:
                    return False
            return True

        for i in range(n + 1, 10**8):
            if is_balanced(i):
                return i
