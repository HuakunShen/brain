# 876. Middle of the Linked List

## Naive Approach

Time Complexity is O(N).

First pass counts the length of linked list.

Then compute midpoint index, iterate linked list again, stop when middle index is reached.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length, cur = 0, head
        while cur is not None:
            length += 1
            cur = cur.next
        mid_idx = length // 2
        cur, cur_idx = head, 0
        while cur_idx < mid_idx:
            cur_idx += 1
            cur = cur.next
        return cur
```

## Fast-Slow Pointer

Since we are looking for middle, we have have 2 pointers.

The fast pointer goes twice as fast as the slow pointer, then when `fast` reaches the end of linked list, `slow` should reach the middle.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow
```
