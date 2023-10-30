# 897. Increasing Order Search Tree

[TOC]

https://leetcode.com/problems/increasing-order-search-tree/

Level: Easy (I feel like this is medium, not so easy if you don't know the trick i.e. inorder traversal)

## Solution

Let $N$ be number of nodes in a given tree.

Below is my solution, where recursion is used and all base cases handled.

Since this is using recursion, every node is gone through exactly once, the Time and Space Complexity are $O(N)$.

### Idea

The `helper` function turns both left and right subtree into "Increasing Order Search Tree", return the head and tail
of the tree. With the head and tail for both left and right subtree, we can easily assemble them with root by setting

1. `left_tail.right = root; root.left = None`
2. `root.right = right_head`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """
        Runtime: 35 ms, faster than 78.67% of Python3 online submissions for Increasing Order Search Tree.
        Memory Usage: 14 MB, less than 13.79% of Python3 online submissions for Increasing Order Search Tree.
        """
        def helper(root: Optional[TreeNode]):
			# base case
            if root is None:
                return None, None
            elif root.left is None and root.right is None:
                return root, root
			# recursive step
            elif root.left is not None and root.right is None:
                head, tail = helper(root.left)
                root.left = None
                tail.right = root
                return head, root
            elif root.right is not None and root.left is None:
                head, tail = helper(root.right)
                root.right = head
                return root, tail
            else:
                left_head, left_tail = helper(root.left)
                root.left = None
                left_tail.right = root
                right_head, right_tail = helper(root.right)
                root.right = right_head
                return left_head, right_tail

        head, tail = helper(root)
        return head
```

## Official Solution

https://leetcode.com/problems/increasing-order-search-tree/solution/

Let $N$ be number of nodes in a given tree.

The 2 official solutions are variants of each other. The different between this and my solution is that the official
solution uses traversal to focus the operation on a "cur" node and the next node in traversal. My solution focused on
handling the cases for 2 subtrees which is more complicated.

### In-Order Traversal

The resulting tree is basically a in order traversal of the BST.

So just traverse through it in order in a DFS pattern and attach each node as the right child of the previous node.

The underlying idea is similar to my solution but much shorter, where left, root, right are arranged in ordered.

Since Another tree is maintained, and every node is traversed through once, Time and Space Complexity are both $O(N)$.

#### Python

```python
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right
```

#### Java

Python syntax is kind of cheating here. It's better to understand how to do in-order traversal in Java

```java
class Solution {
    public TreeNode increasingBST(TreeNode root) {
        List<Integer> vals = new ArrayList();
        inorder(root, vals);
        TreeNode ans = new TreeNode(0), cur = ans;
        for (int v: vals) {
            cur.right = new TreeNode(v);
            cur = cur.right;
        }
        return ans.right;
    }

    public void inorder(TreeNode node, List<Integer> vals) {
        if (node == null) return;
        inorder(node.left, vals);
        vals.add(node.val);
        inorder(node.right, vals);
    }
}
```

### Traversal with Relinking

Similar to previous solution, but tree is altered inplace.

Space Complexity reduced to $O(H)$ where $H$ is the height of the given tree,
and the size of the implicit call stack in our in-order traversal.

#### Python

```python
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
```

#### Java

Python syntax is kind of cheating here. It's better to understand how to do in-order traversal in Java

```java
class Solution {
    TreeNode cur;
    public TreeNode increasingBST(TreeNode root) {
        TreeNode ans = new TreeNode(0);
        cur = ans;
        inorder(root);
        return ans.right;
    }

    public void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
        node.left = null;
        cur.right = node;
        cur = node;
        inorder(node.right);
    }
}
```

## Test Cases

```
[1]
[2,1]
[3,2,null,1]
[3,2,4,1]
[5,3,6,2,4,null,8,1,null,null,null,7,9]
```
