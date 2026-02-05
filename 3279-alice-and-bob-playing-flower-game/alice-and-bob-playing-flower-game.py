class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        count = 0

        odds_in_n = (n + 1) // 2
        even_in_m = m // 2
        count += odds_in_n * even_in_m

        even_in_n = n // 2
        odds_in_m = (m + 1) // 2
        count += even_in_n * odds_in_m

        return count
