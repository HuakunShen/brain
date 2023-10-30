package main


func isInterleave(s1 string, s2 string, s3 string) bool {
    // Runtime: 4 ms, faster than 50.00% of Go online submissions for Interleaving String.
    // Memory Usage: 2.3 MB, less than 18.29% of Go online submissions for Interleaving String.
    l1, l2, l3 := len(s1), len(s2), len(s3)
    if (l3 != l1 + l2) {
        return false;
    }
    dp := make([][]bool, l1 + 1)
    for i := range dp {
        dp[i] = make([]bool, l2 + 1)
    }
    for i := 0; i <= l1; i++ {
        for j := 0; j <= l2; j++ {
            if i == 0 && j == 0 {
                dp[i][j] = true
            } else if i == 0 {
                dp[i][j] = dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]
            } else if j == 0 {
                dp[i][j] = dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]
            } else {
                dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) || (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1])
            }
        }
	}
    return dp[l1][l2]
}


func main() {
    if isInterleave("a", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "a") != false {
        panic("Expecting false, got true")
    }
    if isInterleave("abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb", "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc", "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc") != true {
        panic("Expecting true, got false")
    }
    if isInterleave("aabcc", "dbbca", "aadbbbaccc") != false {
        panic("Expecting false, got true")
    }
    if isInterleave("aabcc", "dbbca", "aadbbcbcac") != true {
        panic("Expecting true, got false")
    }
}