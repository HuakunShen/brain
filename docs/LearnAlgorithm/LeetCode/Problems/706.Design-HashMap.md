# 706. Design HashMap

https://leetcode.com/problems/design-hashmap/

Level: Easy

Similar to [Design HashSet](../705.Design-HashSet/README.md).

Instead of only saving key, we save a List into a slot. The idea is exactly the same.

## Solution

```python
class MyHashMap:
	"""
	Runtime: 302 ms, faster than 68.67% of Python3 online submissions for Design HashMap.
	Memory Usage: 17.2 MB, less than 66.78% of Python3 online submissions for Design HashMap.
	"""
    def __init__(self):
        self.len = 10**3
        self.hashmap = [[] for i in range(self.len)]

    def hash(self, key: int) -> int:
        return key % self.len
            
    def put(self, key: int, value: int) -> None:
        slot = self.hashmap[self.hash(key)]
        for x in slot:
            if x[0] == key:
                print(x)
                x[1] = value
                return
        slot.append([key, value])
    
    def get(self, key: int) -> int:
        slot = self.hashmap[self.hash(key)]
        for x in slot:
            if x[0] == key:
                return x[1]
        return -1
    
    def remove(self, key: int) -> None:
        self.hashmap[self.hash(key)] = list(filter(lambda x: x[0] != key, self.hashmap[self.hash(key)]))


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```