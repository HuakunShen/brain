# 203. Remove Linked List Elements

https://leetcode.com/problems/remove-linked-list-elements/

Level: Easy

Use sentinel to remove first node.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        cur = sentinel
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                continue
            cur = cur.next
        return sentinel.next
```