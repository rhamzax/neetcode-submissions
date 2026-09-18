class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            dfs(j, cur)
        dfs(0,[])
        return res