# 953. Verifying an Alien Dictionary

https://leetcode.com/problems/verifying-an-alien-dictionary/description/

Easy

The question itself is a little hard to understand, but once you understand what it's asking for, it's very simple.

Compare every pair of consecutive words, see if all of the pairs are sorted.

Of course you need to turn the `order` string into a order dictionary with the order in numbers (which is comparable).

For words with the same "prefix", longer word should be the later one. 

When comparing a pair of words, compare each letter. If 2 letters are the same, then keep comparing. 

Otherwise you can decide whether 2 words are sorted based on the current pair of letters.

```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        for i, letter in enumerate(order):
            order_dict[letter] = i
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            l1, l2 = len(w1), len(w2)
            min_l = min(l1, l2)
            for j in range(min_l):
                if order_dict[w1[j]] > order_dict[w2[j]]:
                    return False
                if w1[j] != w2[j]:
                    break
            if w1[:min_l] == w2[:min_l] and l1 > l2:
                return False
        return True
```