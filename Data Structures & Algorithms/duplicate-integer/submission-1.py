class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueChar = set()
        for num in nums:
            uniqueChar.add(num)
        if len(uniqueChar) != len(nums):
            return True
        return False