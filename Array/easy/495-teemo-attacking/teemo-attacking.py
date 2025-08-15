class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ## BruteForce
        # total = duration

        # for i in range(len(timeSeries) - 1):
        #     if timeSeries[i] + duration < timeSeries[i + 1]:
        #         total += duration
        #     else:
        #         total += timeSeries[i + 1] - timeSeries[i]
        # return total

        # Optimal
        total_poison_time = 0
        last_attack_time = -duration

        for attack_time in timeSeries:
            time_since_last_attack = attack_time - last_attack_time
            if time_since_last_attack < duration:
                total_poison_time += time_since_last_attack
            else:
                total_poison_time += duration
            last_attack_time = attack_time
        return total_poison_time
