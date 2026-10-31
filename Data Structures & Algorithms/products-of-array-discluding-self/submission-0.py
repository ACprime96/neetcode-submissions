class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lp, rp = [1] * n, [1] * n
        for i in range(n):
            lp[i] = lp[i-1] * nums[i] if i-1 >= 0 else nums[i]
        for i in range(n-1, -1, -1):
            rp[i] = rp[i+1] * nums[i] if i+1 < n else nums[i]

        res = [0] * n
        for i in range(n):
            l = lp[i-1] if i-1 >= 0 else 1
            r = rp[i+1] if i+1 < n else 1
            res[i] = l * r
        return res