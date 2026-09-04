class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for i in range(len(nums) + 1)]
         #the indexs are how many times it is seen
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, val in count.items():
            buckets[val].append(key)
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
            if(len(res) == k):
                break
        return res