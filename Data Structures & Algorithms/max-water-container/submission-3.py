class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxWater = 0
        while left < right:
            leftSide = heights[left]
            rightSide = heights[right]
            topOfContainer = min(leftSide, rightSide)
            maxWater = max(maxWater, topOfContainer * (right-left))
            if leftSide >= rightSide:
                right -= 1
            else:
                left += 1
        return maxWater