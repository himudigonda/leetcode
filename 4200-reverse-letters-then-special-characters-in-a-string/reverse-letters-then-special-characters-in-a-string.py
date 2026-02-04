class Solution:
    def reverseByType(self, s: str) -> str:
        array = list(s)
        left = 0
        right = len(s) - 1
        spcchar = "!@#$%^&*()"
        # step 1: special char

        while left < right:
            while array[left] not in spcchar and left < right:
                left += 1
            while array[right] not in spcchar and left < right:
                right -= 1
            if array[left] in spcchar and array[right] in spcchar:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1

        left = 0
        right = len(s) - 1
        while left < right:
            while not array[left].isalpha() and left < right:
                left += 1
            while not array[right].isalpha() and left < right:
                right -= 1
            if array[left].isalpha() and array[right].isalpha():
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1

        return "".join(array)
