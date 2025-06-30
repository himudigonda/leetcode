class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        keysPressedArr = [str(i) for i in keysPressed]
        if len(keysPressedArr) != len(releaseTimes):
            return -1

        maxkey = keysPressedArr[0]
        maxduration = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            curduration = releaseTimes[i] - releaseTimes[i - 1]
            if maxduration < curduration:
                maxduration = curduration
                maxkey = keysPressedArr[i]
            if maxduration == curduration:
                if keysPressedArr[i] > maxkey:
                    maxkey = keysPressedArr[i]
        return maxkey
