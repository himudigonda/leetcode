class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def get_num(ch):
            return ord(ch) - ord("a")

        firstnum = []
        for i in firstWord:
            firstnum.append(str(get_num(i)))

        secondnum = []
        for i in secondWord:
            secondnum.append(str(get_num(i)))

        targetnum = []
        for i in targetWord:
            targetnum.append(str(get_num(i)))

        return int("".join(firstnum)) + int("".join(secondnum)) == int("".join(targetnum))
