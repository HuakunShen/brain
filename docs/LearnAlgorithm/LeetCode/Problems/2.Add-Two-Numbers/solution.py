# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(-1)
        curr = result
        l1_curr = l1
        l2_curr = l2
        carry = 0
        while l1_curr or l2_curr or carry:
            s = carry
            if l1_curr:
                s += l1_curr.val
            if l2_curr:
                s += l2_curr.val
            carry = 0
            if s >= 10:
                carry = 1
                curr.val = s % 10
            else:
                curr.val = s
            if l1_curr:
                l1_curr = l1_curr.next
            if l2_curr:
                l2_curr = l2_curr.next
            if l1_curr or l2_curr or carry:
                curr.next = ListNode(-1)
                curr = curr.next
        return result
