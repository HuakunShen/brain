# 844. Backspace String Compare

https://leetcode.com/problems/backspace-string-compare/

Level: Easy

**O(n)**

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def produce(s: str):
            result = []
            for l in s:
                if l == "#":
                    if len(result) != 0:
                        result.pop()
                else:
                    result.append(l)
            return result
        print(produce(s))
        print(produce(t))
        return produce(s) == produce(t)
```