class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # BruteForce
        sorted_scores = sorted(score, reverse = True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank_mapping = {score: medals[i] if i < 3 else str(i + 1) for i, score in enumerate(sorted_scores)}
        return [rank_mapping[a] for a in score]
