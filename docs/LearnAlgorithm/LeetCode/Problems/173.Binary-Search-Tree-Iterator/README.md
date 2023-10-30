# 173. Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

Level: Medium (Actually Easy if you know BST in-order traversal)



## Solution

The idea is very simple, traverse through the BST in order and record all values in a stack.

`hasNext()` returns whether stack is empty.

`next()` returns value popped from stack.

The downside is that you have to store an extra stack with $O(N)$. I haven't think of a way to effectively solve this.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            self.stack.append(root.val)
            inorder(root.right)
        inorder(root)
        self.stack.reverse()

    def next(self) -> int:
        if self.hasNext():
            return self.stack.pop()
            

    def hasNext(self) -> bool:
        return len(self.stack) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```