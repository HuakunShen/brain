# 347. Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/

Level: Medium (should be easy)

## Solution

**Time Complexity:** O(n+k*log(n))

Counting and heapifying both takes O(n) of time. 

Popping from heap `k` times takes O(k log(n)) of time.

A max heap should be used in this question, but in Python only min heap is implemented.

Inverting the number will turn a min heap into a max heap.

Read [Heap Notes](../../../Technique/heap.md).

```python
class Solution:
	"""
	Runtime: 100 ms, faster than 96.24% of Python3 online submissions for Top K Frequent Elements.
	Memory Usage: 18.7 MB, less than 68.16% of Python3 online submissions for Top K Frequent Elements.
	"""
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)											# O(n)
        count_arr = [(-val, key) for key, val in counter.items()]		# O(n)
        heapify(count_arr)												# O(n)
        result = [heappop(count_arr)[1] for i in range(k)]				# O(k*log(n))
        return result
```