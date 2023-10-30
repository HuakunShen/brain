// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


/**
 * Runtime: 4 ms, faster than 96.57% of C++ online submissions for Merge Two Sorted Lists.
 * Memory Usage: 14.8 MB, less than 10.49% of C++ online submissions for Merge Two Sorted Lists.
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* tmp = new ListNode();
        ListNode* cur = tmp;
        ListNode* cur1 = l1;
        ListNode* cur2 = l2;
        while (cur1 && cur2) {
            ListNode* new_node = new ListNode();
            if (cur1->val > cur2->val) {
                new_node->val = cur2->val;
                cur2 = cur2->next;
            } else {
                new_node->val = cur1->val;
                cur1 = cur1->next;
            }
            cur->next = new_node;
            cur = cur->next;
        }
        if (cur1) {
            cur->next = cur1;
            cur = cur->next;
        } else if (cur2) {
            cur->next = cur2;
            cur = cur->next;
        }
        cur = tmp->next;
        delete tmp;
        return cur;
    }
};