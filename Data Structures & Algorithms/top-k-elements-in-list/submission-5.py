class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]
        res = []

        for num, freq in freq_map.items():
            bucket[freq].append(num)

        while k > 0:
            for i in range(len(bucket)-1, -1, -1):
                for n in bucket[i]:
                    if k == 0:
                        return res
                    else:
                        res.append(n)
                        k -= 1

        return res
