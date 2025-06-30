class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxkey = keysPressed[0]
        maxduration = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            curduration = releaseTimes[i] - releaseTimes[i - 1]
            if maxduration < curduration or (
                maxduration == curduration and keysPressed[i] > maxkey
            ):
                maxduration = curduration
                maxkey = keysPressed[i]
        return maxkey
