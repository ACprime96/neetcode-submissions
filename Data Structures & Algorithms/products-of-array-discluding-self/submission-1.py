class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = 1
        suff = 1

        for i in range(len(nums)):
            res[i] = pre # 1,-1,0,0,0
            pre *= nums[i] 
        
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suff #0*1 -> 0*1*3 -> 0*1*3*2 -> -1*1*3*2*1 -> 1*1*3*2*1*0
            suff *= nums[i]

        return res


     