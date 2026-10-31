class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, ArrayList<int[]>> adjList = new HashMap();
        for(int i = 1; i<n+1; i++) {
            adjList.put(i, new ArrayList());
        }
        for(int[] time : times) {
            int u = time[0], v = time[1], t = time[2];
            adjList.get(u).add(new int[] {t, v});
        }
        Queue<int[]> pq = new PriorityQueue<>((n1, n2) -> (n1[0] - n2[0]));
        Map<Integer, Integer> shortest = new HashMap();
        pq.add(new int[] {0, k});
        while(!pq.isEmpty()) {
            int[] temp = pq.remove();
            int w = temp[0], node = temp[1];
            if(shortest.containsKey(node)) {
                continue;
            }
            shortest.put(node, w);
            for(int[] nghrs : adjList.get(node)){
                int w1 = nghrs[0], node1 = nghrs[1];
                if(!shortest.containsKey(node1)) {
                    pq.add(new int[] {w + w1, node1});
                }
            }
        }

        if(shortest.keySet().size() != n) return -1;
        int res = 0;
        for(int src : shortest.keySet()) {
            res = Math.max(res, shortest.get(src));
        }
        return res;
    }
}
