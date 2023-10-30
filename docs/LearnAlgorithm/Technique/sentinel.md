# Sentinel

哨兵

## Linked List

To remove a node in linked list, we usually connect the `next` attribute of the predecessor node to the next node, but when we need to remove the first node, there is not predecessor node.

Sentinel can be added to the front of linked list's head to solve this problem.

## General Code Structure

```python
def solution(head: ListNode):
	sentinel = ListNode(0, head)
	pred = sentinel
	while pred:
		# ... head may be moved somewhere
		pred.next = head
	return sentinel.next
```

See [203.Remove-Linked-List-Elements](../LeetCode/Problems/203.Remove-Linked-List-Elements/README.md) for an example.

# Reference

- [链表中的哨兵是怎么一个作用？](https://www.zhihu.com/question/27155932)

