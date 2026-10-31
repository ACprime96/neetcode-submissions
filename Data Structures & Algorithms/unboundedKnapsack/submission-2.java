class Solution {
    public int maximumProfit(List<Integer> profit, List<Integer> weight, int capacity) {
        int[] cache = new int[capacity + 1];
        for(int i = 0; i<capacity+1; i++) {
            for(int j = 0; j<profit.size(); j++) {
                if(i-weight.get(j) >= 0) {
                    int temp = profit.get(j) + cache[i-weight.get(j)];
                    cache[i] = Math.max(cache[i], temp);
                }
            }
        }
        return cache[capacity];
    }
}
