class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-1):
            left = i + 1
            right = len(nums)-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if curSum > 0:
                    right -=1
                elif curSum < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res

        