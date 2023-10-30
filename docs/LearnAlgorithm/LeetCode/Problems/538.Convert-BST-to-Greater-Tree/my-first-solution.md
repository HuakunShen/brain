[TOC]

# My Solution

My thinking process while tackling this problem is in the method docstring.

Given number of nodes = $N$

Time Complexity: $O(N)$

- One traversal

Space Complexity: $O(N)$

- No extra space used for storing tree
- Recursion takes $O(N)$ space. Each recursive call costs constant space.

![assets/image-20220416033850194.png](./assets/image-20220416033850194.png)

## Python

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

## Golang

```
Runtime: 10 ms, faster than 83.58% of Go online submissions for Convert BST to Greater Tree.
Memory Usage: 6.7 MB, less than 80.60% of Go online submissions for Convert BST to Greater Tree.
```

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func update(root *TreeNode, acc int) int {
    if root == nil {
        return 0
    } else {
        rightSum := update(root.Right, acc)
        newRootVal := root.Val + rightSum + acc
        leftSum := update(root.Left, newRootVal)
        totalSum := root.Val + leftSum + rightSum
        root.Val = newRootVal
        return totalSum
    }
}

func convertBST(root *TreeNode) *TreeNode {
    update(root, 0)
    return root
}
```

## Java

```
Runtime: 1 ms, faster than 83.72% of Java online submissions for Convert BST to Greater Tree.
Memory Usage: 42.2 MB, less than 93.38% of Java online submissions for Convert BST to Greater Tree.
```

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public Integer update(TreeNode root, Integer acc) {
        if (root == null) {
            return 0;
        } else {
            Integer rightSum = update(root.right, acc);
            Integer newRootVal = root.val + rightSum + acc;
            Integer leftSum = update(root.left, newRootVal);
            Integer totalSum = root.val + leftSum + rightSum;
            root.val = newRootVal;
            return totalSum;
        }
    }
    public TreeNode convertBST(TreeNode root) {
        update(root, 0);
        return root;
    }
}
```

## C++

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int update(TreeNode* root, int acc) {
        if (root == NULL) {
            return 0;
        } else {
            int rightSum = update(root->right, acc);
            int newRootVal = root->val + rightSum + acc;
            int leftSum = update(root->left, newRootVal);
            int totalSum = root->val + leftSum + rightSum;
            root->val = newRootVal;
            return totalSum;
        }
    }
    TreeNode* convertBST(TreeNode* root) {
        update(root, 0);
        return root;
    }
};
```

## C

```
Runtime: 22 ms, faster than 84.00% of C online submissions for Convert BST to Greater Tree.
Memory Usage: 13.7 MB, less than 67.00% of C online submissions for Convert BST to Greater Tree.
```

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int update(struct TreeNode* root, int acc) {
    if (root == NULL) {
        return 0;
    } else {
        int rightSum = update(root->right, acc);
        int newRootVal = root->val + rightSum + acc;
        int leftSum = update(root->left, newRootVal);
        int totalSum = root->val + leftSum + rightSum;
        root->val = newRootVal;
        return totalSum;
    }
}

struct TreeNode* convertBST(struct TreeNode* root){
    update(root, 0);
    return root;
}
```

## JavaScript

```
Runtime: 102 ms, faster than 80.16% of JavaScript online submissions for Convert BST to Greater Tree.
Memory Usage: 52 MB, less than 19.84% of JavaScript online submissions for Convert BST to Greater Tree.
```

```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */

var update = (root, acc) => {
  if (root === null) {
    return 0;
  } else {
    const rightSum = update(root.right, acc);
    const newRootVal = root.val + rightSum + acc;
    const leftSum = update(root.left, newRootVal);
    const totalSum = root.val + leftSum + rightSum;
    root.val = newRootVal;
    return totalSum;
  }
};

var convertBST = function (root) {
  update(root, 0);
  return root;
};
```
