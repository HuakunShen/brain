# 2. Add Two Numbers

```python
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
```

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

public class solution_official {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode p = l1, q = l2, curr = dummyHead;
        int carry = 0;
        while (p != null || q != null) {
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if (p != null) p = p.next;
            if (q != null) q = q.next;
        }
        if (carry > 0) {
            curr.next = new ListNode(carry);
        }
        return dummyHead.next;
    }
}
```

```cpp
/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


/**
 * Runtime: 36 ms, faster than 64.67% of C++ online submissions for Add Two Numbers.
 * Memory Usage: 70.3 MB, less than 22.20% of C++ online submissions for Add Two Numbers.
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* cur1 = l1;
        ListNode* cur2 = l2;
        ListNode* head = new ListNode(0);
        ListNode* cur = head;
        short carry = 0;
        while (cur1 || cur2) {
            short x = cur1 ? cur1->val : 0;
            short y = cur2 ? cur2->val : 0;
            short sum = x + y + carry;
            carry = sum / 10;
            cur->next = new ListNode(sum % 10);
            cur = cur->next;
            if (cur1) cur1 = cur1->next;
            if (cur2) cur2 = cur2->next;
        }
        if (carry) {
            cur->next = new ListNode(carry);
        }
        return head->next;
    }
};
```