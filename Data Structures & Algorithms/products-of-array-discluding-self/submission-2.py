class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j != i:
        #             res[i] = res[i] * nums[j]
        # return res
        n = len(nums)
        prefix = [1] * n 
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        res = [1] * n
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res
            