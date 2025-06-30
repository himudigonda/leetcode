class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        if len(keysPressed) != len(releaseTimes):
            return -1

        maxkey = keysPressed[0]
        maxduration = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            curduration = releaseTimes[i] - releaseTimes[i - 1]
            if maxduration < curduration:
                maxduration = curduration
                maxkey = keysPressed[i]
            if maxduration == curduration:
                if keysPressed[i] > maxkey:
                    maxkey = keysPressed[i]
        return maxkey
