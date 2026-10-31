class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        res = 0
        for n in nums:
            if n-1 not in num_set:
                i = 0
                while n in num_set:
                    n += 1
                    i += 1
                    res = max(res, i)

        return res 