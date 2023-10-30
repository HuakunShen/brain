class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        >>> sol = Solution1()
        >>> sol.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab")
        False
        >>> sol.isInterleave("abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb", "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc", "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc")
        True
        >>> sol.isInterleave("aabcc", "dbbca", "aadbbbaccc")
        False
        >>> sol.isInterleave("aabcc", "dbbca", "aadbbcbcac")
        True
        """
        if len(s1) + len(s2) != len(s3):
            return False
        memo = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        # in memoization table, -1 means not visited, 0 means fail, 1 means success

        def helper(i: int, j: int, k: int) -> int:
            sum_remain = len(s1) + len(s2) + len(s3) - i - j - k
            if memo[i][j] != -1:
                pass                    # current cell has been calculated, just return it
            elif sum_remain == 0 or len(s1) - i == 0 and s2[j:] == s3[k:] or len(s2) - j == 0 and s1[i:] == s3[k:]:
                # exit condition and exit early condition
                # no remaining letters every where, or
                # one of s1 and s2 is finished and the other one's remaining letters match with s3's remaining letters
                memo[i][j] = 1
            else:
                first_match, second_match = len(s1) - i and s1[i] == s3[k], len(s2) - j and s2[j] == s3[k]
                first_success = helper(i + 1, j, k + 1) if first_match else False
                second_success = helper(i, j + 1, k + 1) if second_match else False
                memo[i][j] = first_success or second_success
            return memo[i][j]

        return bool(helper(0, 0, 0))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
