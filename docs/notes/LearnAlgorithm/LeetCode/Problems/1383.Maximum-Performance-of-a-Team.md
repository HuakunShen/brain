# 1383. Maximum Performance of a Team



[LeetCode Problem **[hard]**](https://leetcode.com/problems/maximum-performance-of-a-team/)

## Related Topics

- Greedy
- Sort

## Solution: Greedy Algorithm with Priority Queue

Let N be the total number of candidates, and K be the size of the team.

**Time Complexity:** $O(N*(logN + logK))$

   - Build a list of candidates: $O(N)$
- Sort the candidates: $O(N*log(N))$
- In each iteration, the push and pop operation takes $O(log(K-1))$: $O(N * log(K-1))$

**Space Complexity:** $O(N+K)$

    - List of candidates (engineers) has a size of $N$
        - The priority queue (heap) has a capacity of $O(K-1)$
        - The space for sorting is also a factor
        - Timsort: $O(N)$
        - Quicksort: $O(log N)$

```python
from typing import List
import heapq


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        candidates = zip(efficiency, speed)
        candidates = sorted(candidates, key=lambda t: t[0], reverse=True)
        speed_heap = []
        speed_sum, perf = 0, 0
        for cur_efficiency, cur_speed in candidates:
            if len(speed_heap) > k - 1:
                speed_sum -= heapq.heappop(speed_heap)
            heapq.heappush(speed_heap, cur_speed)

            speed_sum += cur_speed
            perf = max(perf, speed_sum * cur_efficiency)
        return perf % (10 ** 9 + 7)
```

This is a short algorithm, but a smart and complex one. The [official solution](https://leetcode.com/problems/maximum-performance-of-a-team/solution/) 
has a long explanation, but it really helps the understanding to the problem.

I will explain what the official solution didn't explain (associate the theory with the code).

The main idea is to iterate through every engineer, assume the current engineer is the one with
the lowest efficiency, then update the maximum performance achieved so far.

The way to approach this idea isn't using a double for loop (where the first for loop is for the fixed lowest-efficiency engineer
and the second loop for the rest of the group of engineers), but with a priority queue (heap).

```python
if len(speed_heap) > k - 1:
    speed_sum -= heapq.heappop(speed_heap)
heapq.heappush(speed_heap, cur_speed)
```

This piece of code is responsible for maintaining the fastest (k-1) speeds/engineers, given that the current engineer must be included.

When the heap is full, we pop one out (the slowest one will be popped out), and we always add the current engineer to the heap.

Since the `candidates` list is sorted reversely by the efficiency, we can guarantee that the current engineer has the lowest efficiency so far.
Since the lowest efficiency is the bottleneck, and all previous engineers are at least as efficient as current engineer,
we just need to keep track of the maximum sum of speeds given the important condition that the current user must be included.

The heap contains the speeds of all previous engineers, the lowest speed is dropped when adding current engineer's speed.
This is how the priority queue works.

`perf` variable keeps track the max performance achieved so far.


## Further Thinking

> If you need to return the indices of the selected engineers instead of only the max performance, what would you do?

1. Include engineer indices while doing zipping and sorting.
2. Include the engineer indices while adding the speeds to the heap. `heappush(h, (5, <index>))`
3. Having a variable keeping a copy of the max-performing group (a heap).
