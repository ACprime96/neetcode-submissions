class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) {
            return 0;
        }
        int l = 0, r = 1;
        int res = prices[r] - prices[l];
        while (r < prices.length) {
            int p = prices[r] - prices[l];
            res = Math.max(p, res);
            if (p < 0) {
                l = r;
                r += 1;
            }
            else {
                r += 1;
            }
        }
        return Math.max(res, 0);
    }
}
