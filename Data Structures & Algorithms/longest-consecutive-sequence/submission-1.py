class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxLength = 0
        for num in seen:
            if num-1 in seen:
                pass
            else:
                counter = 1
                while (num+counter) in seen:
                    counter +=1
                maxLength = max(maxLength, counter)
        return maxLength