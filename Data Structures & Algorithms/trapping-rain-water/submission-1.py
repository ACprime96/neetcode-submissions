class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxArea = 0

        #height = [.   0,2,0,3,1,0,1,3,2,1]
        leftMax = height[l] #  0,2,2,3,3,3,3,3,3,3
        rightMax = height[r] # 3,3,3,3,3,3,3,3,2,1

        
