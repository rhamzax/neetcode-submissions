class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            num = nums[i]
            if left == total - left - num:
                return i
            left += num
        return -1
