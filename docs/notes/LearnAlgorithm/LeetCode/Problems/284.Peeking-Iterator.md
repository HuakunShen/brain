# 284. Peeking Iterator

https://leetcode.com/problems/peeking-iterator/

Level: Medium

Not much to explain. This problem is very easy.

2 ways to do this.
1. Iterate and save all of iterator's value, and implement the functions
2. Method 2 iterates through input iterator while itself is being iterated
   1. This type of solution can avoid saving a copy of values of the original iterator (not the current version, I will implement it)

```python
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.ptr = 0
        self.array = []
        
        
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.ptr >= len(self.array):
            self.array.append(self.iterator.next())
        return self.array[self.ptr]
        

    def next(self):
        """
        :rtype: int
        """
        if self.ptr >= len(self.array):
            self.array.append(self.iterator.next())
        self.ptr += 1
        return self.array[self.ptr - 1]
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iterator.hasNext() or self.ptr < len(self.array)

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
```