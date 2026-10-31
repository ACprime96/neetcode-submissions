class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_map = Counter(nums)
        num_heap = []

        for n, c in num_map.items():
            
            heapq.heappush(num_heap, (c, n))
            while len(num_heap) > k:
                v1, v2 = heapq.heappop(num_heap)
                print(v1, v2)

        return [n[1] for n in num_heap]
            