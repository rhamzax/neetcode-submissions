class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxRect = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                rectangle = (i - index) * height
                maxRect = max(maxRect, rectangle)
                start = index
            stack.append([start, h])
        for i, h in stack:
            rectangle = (len(heights) - i) * h
            maxRect = max(maxRect, rectangle)
        return maxRect
                
