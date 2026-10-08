class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            try:
                y=nums.index(target - num,i+1)
                if y!=0:
                    return [i,y]
            except:
                continue