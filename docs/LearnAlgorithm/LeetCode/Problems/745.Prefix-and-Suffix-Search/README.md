# 745. Prefix and Suffix Search

## Python

Both of the 2 following python solutions timed out.

[Solution 1](./solution1.py)

Two trees are created to store both forward direction and backward direction word.

I call them prefix_tree and suffix_tree.

Then traverse the 2 trees with given prefix and suffix.

[Solution 2](./solution2.py)

Similar to Solution 1, We use a single tree, the key for children is the combination of 2 letters (forward and backward direction).

e.g.
```
abcd
dcba
```
Keys:
- ad
- bc
- cb
- da

[Solution 3](./solution3.py)

A solution copied from discussion.

Very special & smart & tricky solution. Use the debugger to find out.