class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            j = i+1
            k = j+1
            while k < len(nums):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i],nums[j],nums[k]])
                elif nums[i] + nums[j] + nums[k] > 0:
                    break
                k += 1
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
        
        return res
            