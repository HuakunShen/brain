/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
*/

// Runtime: 164 ms, faster than 52.21% of Go online submissions for Palindrome Linked List.
// Memory Usage: 8.9 MB, less than 45.69% of Go online submissions for Palindrome Linked List.

func reverse(head *ListNode) *ListNode {
    if head == nil {
        return nil   
    }
    if head.Next == nil {
        return head   
    }
    var ptr1, ptr2 *ListNode = nil, head
    for ; ptr2 != nil; {
        ptr3 := ptr2.Next
        ptr2.Next = ptr1
        ptr1, ptr2 = ptr2, ptr3
    }
    return ptr1
}

func isPalindrome(head *ListNode) bool {
    slow, fast := head, head
    for ; fast != nil && fast.Next != nil; slow, fast = slow.Next, fast.Next.Next {}
    if fast != nil {
        slow = slow.Next
    }
    
    for reverse_half := reverse(slow); reverse_half != nil; reverse_half, head = reverse_half.Next, head.Next {
        if reverse_half.Val != head.Val {
            return false
        }
    }
    return true
}