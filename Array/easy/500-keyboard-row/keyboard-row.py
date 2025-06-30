class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        mapp = {1: "qwertyuiop", 2: "asdfghjkl", 3: "zxcvbnm"}
        ans = []
        for word in words:
            for row in mapp.values():
                if all([x in row for x in word.lower()]):
                    ans.append(word)
        return ans