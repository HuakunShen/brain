# 703. Kth Largest Element in a Stream

- [703. Kth Largest Element in a Stream](#703-kth-largest-element-in-a-stream)
	- [Solution](#solution)
		- [Trial Solution with heap (will timeout)](#trial-solution-with-heap-will-timeout)
		- [Faster Heap Solution with a Trick](#faster-heap-solution-with-a-trick)
			- [Time Complexity:](#time-complexity)
			- [Space Complexity:](#space-complexity)
		- [Super Short Solution with SortedList](#super-short-solution-with-sortedlist)

https://leetcode.com/problems/kth-largest-element-in-a-stream/

Level: Easy

Related Topic: Heap

Related Problem:

- [https://leetcode.com/problems/last-stone-weight/](https://leetcode.com/problems/last-stone-weight/)
- [Note](../1046.Last-Stone-Weight/README.md)

[Heap Notes](../../../Technique/heap.md)

## Solution

### Trivial Solution with heap (will timeout)

Since python's `heapq` library implements a min heap, I store all the numbers after inverting them (times -1).

When adding a new number, I push the value's opposite value first, and pop k values.

The last popped value is the k-th largest which will be returned. Then push everything back to the queue.

**This will timeout!**

Support `len(nums) == N`, number of times `add` is called = `M`, `k` is the k-th max value to return.

```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-x for x in nums]
        heapify(self.heap)				# make max heap
        self.k = k

    def add(self, val: int) -> int:
        heappush(self.heap, -val)
        backup = [heappop(self.heap) for i in range(self.k)]
        for x in backup:
            heappush(self.heap, x)
        return -backup[-1]
```

### Faster Heap Solution with a Trick

#### Time Complexity:

**O(N*log(N) + M*log(k))** time in total.

- Heapify takes O(N) time in python.
- Each pop or push to heap takes O(log(N)) time.
  - If `k==N`, it takes at most O(N log(N)) to pop
- `__init__` takes O(N + N log(N)) time
- `add` function push once and pop once, which takes O(2 \* log(N)) time
- M `add` costs O(M\*log(k)) time

#### Space Complexity:

Costs O(N + M) to store a heap (regular array) of size `N+M` (initial size N, and M added elements).

Read [Heap Notes](../../../Technique/heap.md) first.

> Runtime: 111 ms, faster than 76.78% of Python3 online submissions for Kth Largest Element in a Stream.
> 
> Memory Usage: 18.5 MB, less than 10.77% of Python3 online submissions for Kth Largest Element in a Stream.

```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapify(self.heap)      # make min heap
        self.k = k
        while len(self.heap) > k:
            # when there are k elements left in a min heap, the next popped value should be the k-th max value
			# the popped items are all smaller than the k-th max, and could never become the k-th max.
			# Because elements are added (no removing), the k-th max could only get larger and larger.
            heappop(self.heap)

    def add(self, val: int) -> int:
		# After pushing an item and popping one, the next element is still the k-th max.
        heappush(self.heap, val)
        if len(self.heap) > self.k:
			# this conditional statement is for avoiding empty queue
            heappop(self.heap)
        # a heap array's index 0 is the next item to be popped, saves time from popping and pushing again
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```

### Super Short Solution with SortedList

> Runtime: 147 ms, faster than 47.73% of Python3 online submissions for Kth Largest Element in a Stream.
> 
> Memory Usage: 18.7 MB, less than 6.16% of Python3 online submissions for Kth Largest Element in a Stream.

Not sure how SortedList is implemented, but whatever is added to the sorted list, it's always in order.

I guess data is stored in a regular list structure to support fastest access (`O(1)`) with index.

In this case, adding a new element takes at least O(log(N)) time. O(N) to perform insertion sort style insertion, or O(log(N)) to perform binary earch, and O(N) to shift elements.

**Time Complexity:** O(N*log(N) + M * N)

**Space Complexity:** O(N + M) to store a regular array.

In other languages without `SortedList` library, we have to impelement a binary search and insertion manually.

See [JavaScript Example](https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/291297/JavaScript-Binary-Search).

```python
from sortedcontainers import SortedList

class KthLargest:

    def __init__(self, k, nums):
        self.k, self.sl = k, SortedList(nums)

    def add(self, val):
        self.sl.add(val)  # Note that sl is a SortedList
        return self.sl[-self.k]  # Note that sl is in ascending order
```
