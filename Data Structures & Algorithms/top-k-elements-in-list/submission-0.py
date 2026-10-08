class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lfq={}
        for i, num in enumerate(nums):
            if num in lfq:
                lfq[num] += 1
            else:
                lfq[num] = 1
        sorlfq=sorted(lfq.keys(), key=lfq.get, reverse=True)
        ansArr=sorlfq[0:k]
        
        return ansArr