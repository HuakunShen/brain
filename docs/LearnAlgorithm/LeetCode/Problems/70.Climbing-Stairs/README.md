# 70. Climbing Stairs

[solution.py](./solution.py)

This is a typical dynamic programming program.

With regular bottom-up dynamic programming, we can achieve a time complexity of O(n) and space complexity of O(n),
because we have to store a array of previous calculated solutions and go through every single one of the index.

```python
class Solution1:
    def climbStairs(self, n: int) -> int:
        M = {1: 1, 2: 2}
        for i in range(3, n + 1):
            M[i] = M[i - 1] + M[i - 2]
        return M[n]
```

Dictnary takes more space, we can use an array instead

```python
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        m = [-1 for _ in range(n + 1)]
        m[1] = 1
        m[2] = 2
        for i in range(3, n + 1):
            m[i] = m[i - 1] + m[i - 2]
        return m[n]
```


The improved version reduces the space complexity to O(1).

As we only sum up the previous 2 values, we don't actually need to store an entire array.

When n is large, it's space-inefficient.

Since we keep only 2 previous values, we just need to keep an array of length = 3.

With modular, we can easily decide which 2 are the previous values and which slot should be filled with the new value.

For example, `(i + 2) % 3` is the index of the slot to be filled with the new calculated value

```python
class Solution3:
    def climbStairs(self, n: int) -> int:
        m = [1, 2, -1]
        for i in range(3, n + 1):
            m[(i + 2) % 3] = m[(i + 1) % 3] + m[i % 3]
        return m[(n + 2) % 3]
```