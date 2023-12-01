# 1721. Swapping Nodes in a Linked List

## Solution

### Solution 1 O(n)

Without modifying node value.

```python
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, cur = 0, head
        # count array length first
        while cur is not None:
            count += 1
            cur = cur.next
        p2_pos = count - k + 1  # calculate position of the second number to swap
        if k == p2_pos:         # when list == [1,2,3] and k == 2, swappnig makes no difference
            return head
        if k > p2_pos:          # [1,2,3,4,5], k = 4, is equivalent to the case where k = 2
            return self.swapNodes(head, p2_pos)
        i, cur, p1, p1_prev, p2, p2_prev = 0, head, None, None, None, None
        p2_pos = count - k + 1
        # find and set pointer for first number, second number and their previous nodes
        while cur is not None:
            if i + 2 == k and k != 1:
                p1_prev = cur
            if i + 2 == p2_pos:
                p2_prev = cur
            i += 1
            if i == k:
                p1 = cur
            if i == p2_pos:
                p2 = cur
            cur = cur.next
        p1_next = p1.next       # make a copy
        if p1_prev:             # when k = 1, p1_prev is None
            p1_prev.next = p2
        p1.next = p2.next
        if p2_prev and p2_prev != p1:	# when list length is 1, p2_prev is None
            p2_prev.next = p1
        if p1_next != p2:       # in case [1,2], k=1: p1_next == p2, will cause a cycle
            p2.next = p1_next
        else:                   # to prevent cycle, handle this special case
            # initial: p1 -> p2
            p2.next = p1
        return p2 if k == 1 else head
        
```

## Solution 2 O(n)

Modify node value directly.

```python
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, cur = 0, head
        while cur is not None:     # count linked list length
            count += 1
            cur = cur.next
        p2_pos = count - k + 1     # find position of the second number to swap
        count, cur = 0, head
        while cur is not None:     # find and set pointers of the 2 numbers to swap
            count += 1
            if count == k:
                p1 = cur
            if count == p2_pos:
                p2 = cur
            cur = cur.next
        # swap nodes' values in place
        p1.val, p2.val = p2.val, p1.val	 # python multiple assignment, no need to save a backup for one of the number
        return head
```

## Test Cases

```
[1,2,3,4,5]
2
[1]
1
[1,2]
1
[1,2]
2
```