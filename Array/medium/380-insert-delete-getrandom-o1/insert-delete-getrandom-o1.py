class RandomizedSet:

    def __init__(self):
        self.mapp = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.mapp:
            self.mapp[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        res = val in self.mapp
        if res:
            index = self.mapp[val]
            lastval = self.arr[-1]
            self.arr[index] = lastval
            self.arr.pop()
            self.mapp[lastval] = index
            del self.mapp[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
