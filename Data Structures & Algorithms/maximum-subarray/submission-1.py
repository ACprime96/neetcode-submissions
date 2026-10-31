class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        s, ms = 0, float("-inf")
        ml, mr = 0, 0
        while r < len(nums):
            s += nums[r]
            if s > ms:
                ms = s
                ml, mr = l, r
            while s < 0 and l <= r:
                s -= nums[l]
                l += 1
            
            # print(l, r, s, ms)
            r += 1
            
        return sum(nums[ml:mr+1])
            
        