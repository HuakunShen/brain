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