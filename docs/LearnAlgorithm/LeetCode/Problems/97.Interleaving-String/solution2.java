class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int s1_len = s1.length(), s2_len = s2.length(), s3_len = s3.length();
        if (s3_len != s1_len + s2_len) {
            return false;
        }
        boolean dp[][] = new boolean[s1_len + 1][s2_len + 1];
        for (int i = 0; i <= s1_len; i++) {
            for (int j = 0; j <= s2_len; j++) {
                if (i == 0 && j == 0) {
                    dp[i][j] = true;
                } else if (i == 0) {
                    // start with s2
                    dp[i][j] = dp[i][j - 1] && s2.charAt(j - 1) == s3.charAt(i + j - 1);
                } else if (j == 0) {
                    // start with s1
                    dp[i][j] = dp[i - 1][j] && s1.charAt(i - 1) == s3.charAt(i + j - 1);
                } else {
                    // if true above and  s1 matches s3 i.e. s2 letter in this column is already used, check row letter
                    // or
                    // if true left and s2 matches s3 i.e. s1 letter in this row is already used, check column letter
                    dp[i][j] = (dp[i - 1][j] && s1.charAt(i - 1) == s3.charAt(i + j - 1)) || (dp[i][j - 1] && s2.charAt(j - 1) == s3.charAt(i + j - 1));
                }
            }
        }
        return dp[s1_len][s2_len];
    }
}