# 202. Happy Number

https://leetcode.com/problems/happy-number/

Level: Easy

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        records = set()
        sum_ = 2
        while sum_ != 1:
            sum_ = sum([int(char)**2 for char in str(n)])
            if sum_ in records:
                return False
            records.add(sum_)
            n = str(sum_)
        return True
```