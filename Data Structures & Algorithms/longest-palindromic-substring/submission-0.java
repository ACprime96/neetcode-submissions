class Solution {
    public String longestPalindrome(String s) {
        int[][] cache = new int[s.length()][s.length()];
        int res = 1;
        int maxi = 0, maxj = 0;
        for(int i = s.length()-1; i>=0; i--) {
            for(int j = i; j<s.length(); j++) {
                if(s.charAt(j) == s.charAt(i)) {
                    if(i+1 <= j-1 && cache[i+1][j-1] == 1) {
                        cache[i][j] = 1;
                    }
                    else if(i+1 > j-1) {
                        cache[i][j] = 1;
                    }
                    if(cache[i][j] == 1 && j-i+1 > res) {
                        res = j - i + 1;
                        maxi = i; maxj = j;
                    }
                }
            }
        }
        // for(int[] arr: cache) {
        //     System.out.println(Arrays.toString(arr));
        // } 
        // System.out.println(String.format("maxi=%s maxj=%s", maxi, maxj));  
        
        return s.substring(maxi, maxj + 1);
    }

}
