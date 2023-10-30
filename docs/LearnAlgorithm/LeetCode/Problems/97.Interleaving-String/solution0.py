class Solution0:
    """
    Timeout
    """
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        >>> sol = Solution0()
        >>> sol.isInterleave("abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb", "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc", "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc")
        True
        >>> sol.isInterleave("aabcc", "dbbca", "aadbbbaccc")
        False
        >>> sol.isInterleave("aabcc", "dbbca", "aadbbcbcac")
        True
        """
        sum_all = len(s1) + len(s2) + len(s3)
        if sum_all == 0:
            return True
        elif len(s3) == 0 and sum_all != 0:
            return False
        else:
            first_match, second_match = len(s1) and s1[0] == s3[0], len(s2) and s2[0] == s3[0]
            first_success = self.isInterleave(s1[1:], s2[0:], s3[1:]) if first_match else False
            second_success = self.isInterleave(s1[0:], s2[1:], s3[1:]) if second_match else False
            return first_success or second_success


if __name__ == '__main__':
    import doctest
    doctest.testmod()
