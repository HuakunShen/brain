# 1046. Last Stone Weight

- [1046. Last Stone Weight](#1046-last-stone-weight)
  - [Solution](#solution)

https://leetcode.com/problems/last-stone-weight/

Level: Easy

Topic: Heap

[Heap Notes](../../../Technique/heap.md)

## Solution

Since python implements a min heap, I invert all numbers (times -1) to mimic a max heap.

Heap is a priority queue.

```python
from typing import List
from heapq import heappush, heappop, heapify


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify(heap := [-x for x in stones])
        while len(heap) > 1:
            heappush(heap, heappop(heap) - heappop(heap))
        return -heap[0]
```
