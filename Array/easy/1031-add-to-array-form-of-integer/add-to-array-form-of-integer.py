class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        carry = 0
        for i in range(n - 1, -1, -1):
            print(i, num[i], k)
            temp = k + num[i]
            num[i] = temp % 10
            k = temp // 10

        while k > 0:
            num.insert(0, k % 10)
            k //= 10
        return num
