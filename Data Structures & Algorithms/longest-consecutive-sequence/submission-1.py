class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set()
        for n in nums:
            if n not in num_set:
                num_set.add(n)
        
        res = 0
        for num in num_set:
            if num-1 not in num_set:
                count = 1
                start = num 
                while start+1 in num_set:
                    start += 1
                    count += 1
                res = max(res, count)

        return res 