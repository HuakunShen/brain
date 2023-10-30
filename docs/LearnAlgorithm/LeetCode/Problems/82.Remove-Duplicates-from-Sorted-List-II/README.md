# 82. Remove Duplicates from Sorted List II

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        p1, p2 = head, head.next
        while p2 is not None and p1.val == p2.val:
            if p2.next is None:
                return None
            to_remove = p1.val
            while p1.val == to_remove:
                p1 = p2
                p2 = p2.next
                head = p1
        while p2 is not None:
            while p2.next and p2.next.next and p2.next.val == p2.next.next.val:
                p2.next = p2.next.next.next
            p2 = p2.next
        return head
```

## Test Cases

```
[1,2,3,3,4,4,5]
[1,1]
[1,1,1]
[1,1,2]
[]
[1,2,2]
```