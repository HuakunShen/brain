class Solution:
    """
    Runtime: 24 ms, faster than 98.77% of Python3 online submissions for Longest Common Prefix.
    Memory Usage: 14 MB, less than 40.09% of Python3 online submissions for Longest Common Prefix.

    One 2 passes through the "strs" array, runtime O(n) assuming min_length of strs is constant.
    Otherwise, let "L" be the min length of strs, Worst Case Runtime should be O(n x L)
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs): return ""
        min_len = float("inf")
        for s in strs:
            min_len = min(min_len, len(s))
        i = 0
        while i < min_len:
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return s[:i]
            i += 1
        return strs[0][:i]