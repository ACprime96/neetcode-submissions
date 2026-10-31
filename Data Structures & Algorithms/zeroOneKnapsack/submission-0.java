class Solution {
    public int maximumProfit(List<Integer> profit, List<Integer> weight, int capacity) {
        int[][] cache = new int[profit.size()][capacity+1];
        return maximumProfitHelper(0, profit, weight, capacity, cache);
    }
    public int maximumProfitHelper(int index, List<Integer> profit, List<Integer> weight, int capacity, int[][] cache) {
        if(index == profit.size()) return 0;

        if(cache[index][capacity] != 0) return cache[index][capacity];

        // skip the item
        int maxProfit = maximumProfitHelper(index + 1, profit, weight, capacity, cache);

        int newCapacity = capacity - weight.get(index);
        if(newCapacity >= 0) {
            int p = profit.get(index) + maximumProfitHelper(index + 1, profit, weight, newCapacity, cache);
            maxProfit = Math.max(p, maxProfit);            
        }

        cache[index][capacity] = maxProfit;

        return cache[index][capacity];
    }
}
