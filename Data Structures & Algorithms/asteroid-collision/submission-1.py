class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for n in asteroids:
            while stack and n < 0 and stack[-1] > 0:
                diff = stack[-1] + n
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    n = 0
                else:
                    n = 0
                    stack.pop()
            if n:
                stack.append(n)
        return stack