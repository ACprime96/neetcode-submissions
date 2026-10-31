class PQEntry:
    def __init__(self, cost, row, col):
        self.cost = cost
        self.row = row
        self.col = col

    def __lt__(self, other):
        return self.cost > other.cost

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        pq = [PQEntry(grid[0][0], 0,0)]
        costs = set()
        while pq:
            top = heapq.heappop(pq)
            if (top.row, top.col) in costs:
                continue
            
            if (top.row, top.col) == (len(grid) - 1, len(grid[0]) - 1):
                return top.cost
            
            costs.add((top.row, top.col))
            i,j = top.row, top.col
            neighbors = [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]
            for i1,j1 in neighbors:
                if (
                    not 0 <= i1 < len(grid)
                    or not 0 <= j1 < len(grid[0])
                    or (i1,j1) in costs
                ):
                    continue
                
                heapq.heappush(pq, PQEntry(min(grid[i1][j1] , top.cost), i1,j1))
