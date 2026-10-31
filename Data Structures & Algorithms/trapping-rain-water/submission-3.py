class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        [0,2,0,3,1,0,1,3,2,1]
        [0,2,2,3,3,3,3,3,3,3] prefix
        [3,3,3,3,3,3,3,3,2,1] suffix
        '''
        if len(height) < 3:
            return 0

        l, r = 0, len(height) - 1
        l_max = height[l] # 0
        r_max = height[r] # 1
        res = 0

        while l < r:
            if l_max <= r_max:
                res += min(l_max, r_max) - height[l] # 0,-1,2
                l += 1
                l_max = max(l_max, height[l]) # 1,2
            else:
                res += min(l_max, r_max) - height[r] # 0
                r -= 1 
                r_max = max(r_max, height[r]) # 2,
        
        return res

