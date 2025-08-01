class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        # self.dict[key].append([value, timestamp])
        self.dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # res = ""
        # values = self.dict.get(key, [])
        # left, right = 0, len(values) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if values[mid][1] <= timestamp:
        #         left = mid + 1
        #         res = values[mid][0]
        #     else:
        #         right = mid - 1
        # return res

        dictionary = self.dict
        if key not in dictionary:
            return ""

        arr = dictionary[key]
        left, right = 0, len(arr) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            cur = arr[mid][1]
            if cur == timestamp:
                return arr[mid][0]
            elif cur < timestamp:
                res = arr[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
