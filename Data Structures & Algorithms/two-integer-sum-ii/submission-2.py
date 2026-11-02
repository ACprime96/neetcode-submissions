class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # l = 0
        # for r, n in enumerate(numbers):

        l, r = 0, 1
        while r < len(numbers):
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            if target - numbers[r] > numbers[r]:
                r += 1
            else:
                l += 1
            if l == r:
                r += 1
        return [-1, -1]
        