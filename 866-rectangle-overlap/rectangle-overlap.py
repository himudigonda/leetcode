class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # overlapHeight = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        # overlapWidth = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
        # return overlapHeight > 0 and overlapWidth > 0

        return not (
            rec1[2] <= rec2[0]
            or rec1[0] >= rec2[2]
            or rec1[1] >= rec2[3]
            or rec1[3] <= rec2[1]
        )
