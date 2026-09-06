class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            leftNum = numbers[left]
            rightNum = numbers[right]
            if target == (leftNum + rightNum):
                return [left + 1, right + 1]
            elif target - rightNum > leftNum:
                left+=1
            else:
                right-=1
