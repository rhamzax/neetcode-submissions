class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for pos, speed in pair:
            time = (target - pos) / speed
            if stack and time > stack[-1]:
                stack.append(time)
            if not stack:
                stack.append(time)
        return len(stack)