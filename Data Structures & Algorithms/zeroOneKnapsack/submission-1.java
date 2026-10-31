class Solution {
    public int maximumProfit(List<Integer> profit, List<Integer> weight, int capacity) {
        int[][] cache = new int[profit.size()][capacity+1];
        int p1, p2;
        for(int i = 0; i<profit.size(); i++) {
            for(int j = 0; j<capacity+1; j++) {
                p1 = (i-1 >= 0)? cache[i-1][j] : 0;
                p2 = 0;
                if(j - weight.get(i) >= 0) {
                    p2 = profit.get(i);
                    p2 += (i-1 >= 0)?  cache[i-1][j-weight.get(i)] : 0;
                }
                cache[i][j] = Math.max(p1, p2);
            }
        }
        return cache[profit.size() - 1][capacity];
    }
}
