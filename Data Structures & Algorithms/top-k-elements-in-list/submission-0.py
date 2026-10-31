class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_map = Counter(nums)
        num_heap = []
        res = []
        for n, c in num_map.items():
            heapq.heappush(num_heap, (-c, n))
        
        while num_heap and k > 0:
            _, num = heapq.heappop(num_heap)
            res.append(num)
            k -= 1
        
        return res

            
        
        return res 
            