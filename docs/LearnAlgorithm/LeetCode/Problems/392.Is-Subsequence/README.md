# 392. Is Subsequence

https://leetcode.com/problems/is-subsequence/

Level: Easy

[solution.py](./solution.py)

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

```
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
```

```python
class Solution:
    """
    Runtime: 42 ms, faster than 63.19% of Python3 online submissions for Is Subsequence.
    Memory Usage: 13.8 MB, less than 92.79% of Python3 online submissions for Is Subsequence.
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j = j + 1
                if j >= len(s):
                    return True
        return False
```

# Explanation

Iterate through `t` and keep track of every matched letter in `s` with a pointer.
If the pointer reached the end of `s`, then it's a subsequence, and return `Ture`.
