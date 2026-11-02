class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_map = Counter(nums)
        num_heap = []

        for n, c in num_map.items():
            while len(num_heap) <= k:
                heapq.heappush(num_heap, (c, n))
            heapq.heappop(num_heap)

        return [n[1] for n in num_heap]
            