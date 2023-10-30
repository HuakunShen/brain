# 680. Valid Palindrome II

[Problem](https://leetcode.com/problems/valid-palindrome-ii/)

## Recursion

```python
class Solution:
    """
    Runtime: 7256 ms, faster than 5.01% of Python3 online submissions for Valid Palindrome II.
    Memory Usage: 645.7 MB, less than 5.10% of Python3 online submissions for Valid Palindrome II.
    """
    quota = 1
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 0: return True
        if s[0] == s[-1]:
            return self.validPalindrome(s[1:-1])
        elif self.quota == 0:
            return False
        else:
            self.quota -= 1
            if s[0] == s[-2] or s[1] == s[-1]:
                return self.validPalindrome(s[0:-1]) or self.validPalindrome(s[1:])
            else:
                return False
```

## Two Pointers

```python
class Solution:
    """
    Runtime: 166 ms, faster than 62.31% of Python3 online submissions for Valid Palindrome II.
    Memory Usage: 14.6 MB, less than 19.85% of Python3 online submissions for Valid Palindrome II.
    """
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(sub_s: str):
            s, e = 0, len(sub_s) - 1
            while s < e:
                if sub_s[s] != sub_s[e]:
                    return False
                s += 1
                e -= 1                    
            return True
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return checkPalindrome(s[start + 1:end + 1]) or checkPalindrome(s[start:end])
            start += 1
            end -= 1
        return True

```