# 1071. Greatest Common Divisor of Strings

## Brute Force Solution

Time: $O(n^2)$

The most trivial way to me is to loop through each substring, and check if the substring is a divisor of each string using for loop.

In this process, there can be a few optimization,

1. Take substring from the min-length string
2. Check if substring length is a common divisor, if not, `continue` in loop.

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        divisor = ""
        longest_divisor = ""
        n1, n2 = len(str1), len(str2)
        min_str = str1 if n1 < n2 else str2
        max_str = str1 if n1 >= n2 else str2

        for i in range(min(n1, n2)):
            divisor += min_str[i]
            d_len = len(divisor)
            if n1 % d_len != 0 or n2 % d_len != 0:
                continue
            s1_good, s2_good = True, True
            for j in range(0, n1, d_len):
                if str1[j:j+d_len] != divisor:
                    s1_good = False
            for j in range(0, n2, d_len):
                if str2[j:j+d_len] != divisor:
                    s2_good = False
            print(i, s1_good, s2_good)
            if s1_good and s2_good:
                longest_divisor = divisor
        return longest_divisor

```

## Small Improvement

I noticed that if there is a common divisor (divides both `str1` and `str2`), then it should also divide `str1 + str2`.

The 2 inner for loops in the first solutions can be simplied to the `is_divisor()`.

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_divisor(s: str, d: str) -> bool:
            for i in range(0, len(s), len(d)):
                if s[i:i + len(d)] != d:
                    return False
            return True

        for i in range(min(len(str1), len(str2)), 0, -1):
            if n1 % i != 0 or n2 % i != 0:
                continue
            if is_divisor(str1 + str2, str1[:i]):
                return str1[:i]

        return ""

```

## O(m+n) Solution

I noticed that if 2 strings has a common divisor, then it has to be the one with the greatest length, cannot be shorter divisor.

Let's try to make 2 strings with length 8 and 4. The Greatest Common Divisor can only have length from 1, 2, 4. Can we make the divisor 1 or 2 instead of 4?

No. If the longest divisor has a length of 2. Double it to get length 4, then the divisor when length 4 is the greater common divisor.

Consider `ABABABAB` and `ABAB`.

Same for length 1 divisor.

So we can skip the for loop, and achieve $\mathcal{O}(m+n)$ runtime.

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_divisor(s: str, d: str) -> bool:
            for i in range(0, len(s), len(d)):
                if s[i:i + len(d)] != d:
                    return False
            return True

        n1, n2 = len(str1), len(str2)
        gcd = math.gcd(n1, n2)
        if is_divisor(str1 + str2, str1[:gcd]):
            return str1[:gcd]
        # for i in range(math.gcd(n1, n2), 0, -1):
        #     if n1 % i != 0 or n2 % i != 0:
        #         continue
        #     if is_divisor(str1 + str2, str1[:i]):
        #         return str1[:i]
        return ""

```

## Further Simplified

Another property is that, if 2 strings have common divisor, then `str1 + str2 != str2 + str1` must be true.

If `divisor` divides both strings, then repeating it multiple times give us both `str1` and `str2`. Suppose the times are `i` and `j`, then repeating `i+j` will give us `str1 + str2`.

Given this property and the previous property that "if there is a string GCD, then its length must be also GCD of the 2 strings' length", combining these 2 properties gives us the following solution, which is still $\mathcal{O}(m+n)$, but theoretically a little faster by avoiding the for loop. And of course cleaner.

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:math.gcd(len(str1), len(str2))]
```

## One Liner

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return "" if str1 + str2 != str2 + str1 else str1[:math.gcd(len(str1), len(str2))]
```
