class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # # BruteForce
        # stack = []
        # for stone1 in asteroids:
        #     while stack and stone1 < 0 and stack[-1] > 0:
        #         diff = stone1 + stack[-1]
        #         if diff < 0:
        #             stack.pop()
        #         elif diff > 0:
        #             stone1 = 0
        #         else:
        #             stone1 = 0
        #             stack.pop()
        #     if stone1:
        #         stack.append(stone1)
        # return stack

        # Optimal
        stack = []
        for stone in asteroids:
            while stack and stone < 0 < stack[-1]:
                if stack[-1] < -stone:
                    stack.pop()
                    continue
                elif stack[-1] == -stone:
                    stack.pop()
                break
            else:
                stack.append(stone)
        return stack
