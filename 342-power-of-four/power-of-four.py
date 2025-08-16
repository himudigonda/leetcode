class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # # Recursion
        # if n ==1:
        #     return True
        # if n<=0 or n %4:
        #     return False
        # return self.isPowerOfFour(n //4)

        # Optimal
        return (n & (n - 1)) == 0 and n % 3 == 1

        # Log Method
        # return n > 0 and log(n, 4) % 1 == 0