# 538. Convert BST to Greater Tree

[TOC]



https://leetcode.com/problems/convert-bst-to-greater-tree/

Level: Medium

[My First Recursive Solution](./my-first-solution.md)

## Solution

### Python

```
Runtime: 75 ms, faster than 98.41% of Python3 online submissions for Convert BST to Greater Tree.
Memory Usage: 16.9 MB, less than 29.01% of Python3 online submissions for Convert BST to Greater Tree.
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        The left children will be updated based on accumulated values on the right children
        To make the algorithm more efficient, for the right subtree, we must use a bottom-up approach
        i.e. accumulate from leaves upwards using recursion
        On the contrary, the left subtree will need a top-down approach where the sum is passed down to the children.
        This will also be a recursion, but requires a helper function with an extra "acc" parameter
        The helper function can also be reused for the right subtree by setting "acc" param to 0
        """
        def update(root: Optional[TreeNode], acc: int):
            if root is None:
                # Base Case
                return 0
            else:
                # Recursive Step
                right_sum = update(root.right, acc)
                new_root_val = root.val + right_sum + acc
                left_sum = update(root.left, new_root_val)
                total_sum = root.val + left_sum + right_sum
                # print(f"root.val: {root.val}, acc: {acc}, left_sum: {left_sum}, right_sum: {right_sum}, total_sum: {total_sum}") # debug message
                root.val = new_root_val
                return total_sum
                
        update(root, 0)
        return root
```

## Official Solution

### Recursion

$O(n)$ for both Time and Space Complexity.

```
Runtime: 89 ms, faster than 79.93% of Python3 online submissions for Convert BST to Greater Tree.
Memory Usage: 16.5 MB, less than 97.31% of Python3 online submissions for Convert BST to Greater Tree.
```

```python
class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root
```

### Iteration with a Stack

$O(n)$ for both Time and Space Complexity.

```
Runtime: 85 ms, faster than 85.07% of Python3 online submissions for Convert BST to Greater Tree.
Memory Usage: 16.9 MB, less than 29.01% of Python3 online submissions for Convert BST to Greater Tree.
```

```python
class Solution(object):
    def convertBST(self, root):
        total = 0
        
        node = root
        stack = []
        while stack or node is not None:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            # all nodes with values between the current and its parent lie in
            # the left subtree.
            node = node.left

        return root
```

### Reverse Morris In-order Traversal

- $O(1)$ Space Complexity
- $O(N)$ Time Complexity


```python
class Solution(object):
    def convertBST(self, root):
        # Get the node with the smallest value greater than this one.
        def get_successor(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ
                
        total = 0
        node = root
        while node is not None:
            # If there is no right subtree, then we can visit this node and
            # continue traversing left.
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            # If there is a right subtree, then there is a node that has a
            # greater value than the current one. therefore, we must traverse
            # that node first.
            else:
                succ = get_successor(node)
                # If there is no left subtree (or right subtree, because we are
                # in this branch of control flow), make a temporary connection
                # back to the current node.
                if succ.left is None:
                    succ.left = node
                    node = node.right
                # If there is a left subtree, it is a link that we created on
                # a previous pass, so we should unlink it and visit this node.
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left
        
        return root
```