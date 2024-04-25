# 705. Design HashSet

https://leetcode.com/problems/design-hashset/

Level: Easy

This problem is easy if you've learnt the theory of hash table. I learnt it in CSC263.

Basically there is a time vs space tradeoff.

The ultimate goal is for every operation to have an **Average** runtime of $O(1)$.

The more memory you assign to the hash table, the faster it is.

Suppose you give the hash table a length of 1000, you need a hash function that can theoretically distribute any input
into the 1000 slots with equal probability. Each slot is another array/linked list. 

`contains()` and `remove()` method will require iterating through the array/linked list in a given slot. 
We expect this time to be constant (which isn't always true). 
If the hash function works properly, then the theoretical average runtime is constant.

Linked List will theoretically be faster than regular array while removing an item, but both 
takes $O(N)$ time because of the linear search. You may make each slot sorted and use Binary Search to speed up 
searching (`contains()` and `remove()`), but `add()` will be $O(N)$ instead of $O(1)$ to perform a insertion (linear search).

There are many tradeoffs.

## Solution

```python
class MyHashSet:
	"""
	Runtime: 184 ms, faster than 85.21% of Python3 online submissions for Design HashSet.
	Memory Usage: 19.3 MB, less than 52.37% of Python3 online submissions for Design HashSet.
	"""

    def __init__(self):
        self.hashtable = [[] for i in range(10**3)]

    def hash_func(self, key: int):
        return key % 10**3
        
    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashtable[self.hash_func(key)].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashtable[self.hash_func(key)].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hashtable[self.hash_func(key)]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```