/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/**
 * Runtime: 4 ms, faster than 96.78% of C++ online submissions for Reverse Linked List.
 * Memory Usage: 7.8 MB, less than 99.74% of C++ online submissions for Reverse Linked List.
 */
class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        if (!head) return NULL;
        if (!head->next) return head;
        ListNode *ptr1 = NULL;
        ListNode *ptr2 = head;
        while (ptr2)
        {
            ListNode *ptr3 = ptr2->next;
            ptr2->next = ptr1;
            ptr1 = ptr2;
            ptr2 = ptr3;
        }
        return ptr1;
    }
};

/**
 * Iterative Approach, fast
 * Runtime: 4 ms, faster than 96.78% of C++ online submissions for Reverse Linked List.
 * Memory Usage: 7.8 MB, less than 97.28% of C++ online submissions for Reverse Linked List.
 */
class Solution1
{
public:
    ListNode *reverseList(ListNode *head)
    {
        if (!head)
            return NULL;
        if (!head->next)
            return head;
        ListNode *ptr1 = head;
        ListNode *ptr2 = head->next;
        ListNode *ptr3 = head->next->next;
        head->next = NULL;
        while (ptr3)
        {
            ptr2->next = ptr1;
            ptr1 = ptr2;
            ptr2 = ptr3;
            ptr3 = ptr3->next;
        }
        ptr2->next = ptr1;
        return ptr2;
    }
};

/**
 * Recursion Fast, inplace changes
 * Runtime: 4 ms, faster than 96.78% of C++ online submissions for Reverse Linked List.
 * Memory Usage: 8.1 MB, less than 22.57% of C++ online submissions for Reverse Linked List.
 */
class Solution2
{
public:
    ListNode *reverseList(ListNode *head)
    {
        if (!head || !head->next)
            return head;
        ListNode *reversed = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return reversed;
    }
};

/**
 * Recursion Slow, new Nodes created on heap
 * Runtime: 36 ms, faster than 6.78% of C++ online submissions for Reverse Linked List.
 * Memory Usage: 8.5 MB, less than 5.19% of C++ online submissions for Reverse Linked List.
 */
class Solution3
{
public:
    ListNode *reverseList(ListNode *head)
    {
        if (!head || !head->next)
            return NULL;
        ListNode *node = new ListNode(head->val);
        ListNode *reversed = reverseList(head->next);
        if (!reversed)
            return node;
        ListNode *cur = reversed;
        while (cur && cur->next)
        {
            cur = cur->next;
        }
        if (cur)
            cur->next = node;
        return reversed;
    }
};
