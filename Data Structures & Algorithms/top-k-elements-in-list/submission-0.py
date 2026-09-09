class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        cnt=Counter(nums)
        c=sorted(cnt,key=cnt.get,reverse=True)
        return c[:k]