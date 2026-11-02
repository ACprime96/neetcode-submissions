class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        { 1: 1, 2: 2, 3: 3}

        '''
        freq_map = Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]
        res = []

        for k,v in freq_map.items():
            bucket[v].append(k)
        while k > 0:
            for i in range(len(bucket)-1, -1, -1):
                for n in bucket[i]:
                    if k > 0:
                        res.append(n)
                        k -= 1
                    else:
                        return res

        return res
