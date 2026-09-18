class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            # #Include itself
            # subset.append(nums[i])
            # dfs(i, total + nums[i])

            # subset.pop()
            # dfs(i + 1, total)
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                subset.append(nums[j])
                dfs(j, total + nums[j])
                subset.pop()
        dfs(0, 0)
        return res
            