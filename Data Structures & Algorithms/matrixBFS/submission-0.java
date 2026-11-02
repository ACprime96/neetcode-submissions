class Solution {
    public int shortestPath(int[][] grid) {
        int ROWS = grid.length, COLS = grid[0].length;
        int[][] visited = new int[ROWS][COLS];
        Deque<int[]> q = new ArrayDeque();
        q.addLast(new int[2]);
        visited[0][0] = 1;
        int res = -1;
        while(!q.isEmpty()) {
            res++;
            int len = q.size();
            for(int i = 0; i<len; i++) {
                int[] pos = q.removeFirst();
                if(pos[0] == ROWS - 1 && pos[1] == COLS -1) {
                    return res;
                }
                int[][] dir = {{0,1},{1,0},{-1,0},{0,-1}};
                for(int[] delta: dir) {
                    int r = pos[0] + delta[0];
                    int c = pos[1] + delta[1];
                    if(Math.min(r,c) < 0 || r == ROWS || c == COLS || visited[r][c] == 1) {
                        continue;
                    }
                    q.addLast(new int[] {r,c});
                    visited[r][c] = 1;
                }

            }
        }
        return -1;
        
    }

}
