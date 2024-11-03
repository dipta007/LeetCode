class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            broken = False
            while stack and (a < 0 and stack[-1] > 0):
                if abs(a) > stack[-1]:
                    stack.pop()
                elif abs(a) == stack[-1]:
                    stack.pop()
                    broken = True
                    break
                else:
                    broken = True
                    break
            if not broken:
                stack.append(a)

        return stack