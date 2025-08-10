class Solution:
    power_of_2_digit_str = None

    def _get_sorted_digits(self, num: int) -> str:
        return "".join(sorted(str(num)))

    def reorderedPowerOf2(self, n: int) -> bool:
        # # BruteForce
        # string_n = str(n)
        # for permutation_tuple in permutations(string_n):
        #     permutation_string = "".join(permutation_tuple)
        #     if permutation_string[0] == "0":
        #         continue
        #     num = int(permutation_string)
        #     if num > 0 and (num & (num - 1)) == 0:
        #         return True
        # return False

        # Optimal
        if Solution.power_of_2_digit_str is None:
            Solution.power_of_2_digit_str = set()
            power = 1
            for _ in range(34):
                Solution.power_of_2_digit_str.add(self._get_sorted_digits(power))
                power *= 2
        n_sorted_digits = self._get_sorted_digits(n)
        return n_sorted_digits in Solution.power_of_2_digit_str
