class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def search(num):
            l, r = 0, len(numbers)
            while l<=r:
                m = (l+r)//2

                if  numbers[m] == num :
                    return m
                elif numbers[m] > num:
                    r = m - 1
                else:
                    l = m + 1
            return -1
        
        for i, n in enumerate(numbers):
            diff = target - n
            val = search(diff)
            if val != -1:
               return [i+1, val+1]

        return [-1,-1]  

                