class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(len(nums)):
                if i+k <= len(nums):

                    res.append(max(nums[i:i+k])) 

        
        return res