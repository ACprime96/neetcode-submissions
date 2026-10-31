class Solution {
    public boolean isAnagram(String s, String t) {
        int[] scount  = new int[26];
        int[] tcount = new int[26];
        this.fillCount(s, scount);
        this.fillCount(t, tcount);
        for(int i = 0; i < 26; i++) {
            if(scount[i] != tcount[i]) {
                return false;
            }

        }
        return true;
    }

    public void fillCount(String s, int[] counts)
    {
        for(int i = 0; i<26; i++)
        {
            counts[i] = 0;
        }
        for(int i = 0; i<s.length(); i++)
        {
            counts[s.charAt(i) - 97] += 1;
        }
    }
}
