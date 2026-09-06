class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stack_temp = stack.pop()
                print(stack_temp)
                result[stack_temp[1]] = i - stack_temp[1]
            stack.append([temp, i])
        return result
            
