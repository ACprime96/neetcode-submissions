class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax, rmax = [0] * n, [0] * n
        for i in range(1, n):
            lmax[i] = max(lmax[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            rmax[i] = max(rmax[i+1], height[i+1])
        
        res = 0
        for i, h in enumerate(height):
            if h < lmax[i] and h < rmax[i]:
                minh = min(lmax[i], rmax[i])
                res += minh - h
        
        return res
