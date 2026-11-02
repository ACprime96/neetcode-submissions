class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [max(nums)]
        elif len(nums) == 2:
            return [max(nums), max(nums[1:])]
        elif len(nums) == 2:
            return [max(nums), max(nums[1:]), nums[2]]

        res = []
        for r in range(len(nums)-2):
            if r+1 < len(nums) and r+2 < len(nums):
                res.append(max(nums[r : r+3]))
        
        return res

        