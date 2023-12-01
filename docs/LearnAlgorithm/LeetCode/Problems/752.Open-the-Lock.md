# 752. Open the Lock

[LeetCode Problem](https://leetcode.com/problems/open-the-lock/)

## Solution with BFS

[Python Solution](./solution.py)

```python
from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadend_set = set(deadends)
        if "0000" in deadend_set:
            return -1

        def increment(index: int, current: str, diff: int):
            to_incr = current[index]
            new_val = str((int(to_incr) + diff + 10) % 10)
            return current[:index] + new_val + current[index + 1:]

        def neighbors(code):
            for diff in [-1, 1]:
                for i in range(4):
                    yield increment(i, code, diff)

        q = deque(["0000"])
        steps = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return steps
                for new in neighbors(curr):
                    if new not in deadend_set:
                        deadend_set.add(new)
                        q.append(new)
            steps += 1
        return -1
```