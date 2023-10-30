# Heap

## Complexity

- Get min or max element in O(1) time for min and max heap. If stored as array, that's `arr[0]`.
- Push to or pop from a heap takes O(log(n)) time. Need to traverse tree height which is log(n).

## Tips

-  Construct max heap with a min heap function
	- Push the opposite number (-1 * x) to the heap
	- times the popped value by -1
	- [1046. Last Stone Weight](../LeetCode/Problems/1046.Last-Stone-Weight/README.md)
- When size of a **min heap** is `k`, the next popped value is The k-th **largest** in the heap.
	- This could be a trick to save time.
	- [703. Kth Largest Element in a Stream](../LeetCode/Problems/703.Kth-Largest-Element-in-a-Stream/README.md)

