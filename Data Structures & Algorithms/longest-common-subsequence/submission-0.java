class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] cache = new int[text1.length()][text2.length()];
        dfsHelper(0, 0, text1, text2, cache);
        return cache[0][0];
    }
    public int dfsHelper(int i, int j, String text1, String text2, int[][] cache) {
        if(i == text1.length() || j == text2.length()) {
            return 0;
        }

        if(cache[i][j] != 0) return cache[i][j];
        if(text1.charAt(i) == text2.charAt(j)) {
            cache[i][j] = 1 + dfsHelper(i+1, j+1, text1, text2, cache);
        } else {
            cache[i][j] = Math.max(dfsHelper(i+1, j, text1, text2, cache), dfsHelper(i, j+1, text1, text2, cache));
        }
        return cache[i][j];
    }
    
}
