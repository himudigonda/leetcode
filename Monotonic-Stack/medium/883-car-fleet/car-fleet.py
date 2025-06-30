class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        size = len(position)
        cars = sorted(zip(position, speed), reverse = True)
        fleet = 0
        prev = -1

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > prev:
                fleet += 1
                prev = time
        return fleet
