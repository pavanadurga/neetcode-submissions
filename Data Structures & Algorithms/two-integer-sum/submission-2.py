class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            p=target-nums[i]
            if p in d:
                return sorted([i,d[p]])
            d[nums[i]]=i
