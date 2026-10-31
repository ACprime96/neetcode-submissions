class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] cache = new int[text1.length() + 1][text2.length() + 1];
        int temp1, temp2, temp3;
        for(int i = 1; i<text1.length() + 1; i++) {
            for(int j = 1; j<text2.length() + 1; j++) {
                temp1 = 0; temp2 = 0; temp3 = 0;
                if(text1.charAt(i-1) == text2.charAt(j-1)) {
                    temp1 = 1 + cache[i-1][j-1];
                }
                else {
                    temp2 = cache[i-1][j];
                    temp3 = cache[i][j-1];
                }
                cache[i][j] = Math.max(temp1, Math.max(temp2, temp3));
            }
        }   
        return cache[text1.length()][text2.length()];
    }
}
