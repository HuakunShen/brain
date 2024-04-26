# 1551. Minimum Operations to Make Array Equal

[LeetCode Problem](https://leetcode.com/problems/minimum-operations-to-make-array-equal/)

Medium

This is a Math problem.

Since the array is guaranteed to be able to be averaged, we can simply count the sum of difference between all numbers smaller than average and the average.

## Mehthod 1:

Time Complexity: O(n)

Space Complexity: O(1)

```python
class Solution:
    def minOperations(self, n: int) -> int:
        less_count = 0
        for i in range(n):
            num = 2*i+1
            if num > n:
                less_count += num - n
        return less_count
```

```cpp
class Solution {
public:
    int minOperations(int n) {
        int less_count = 0;
        for(int i = 0; i < n; i++) {
            int num = 2*i+1;
            if (num > n) {
                less_count += num - n;                
            }
        }
        return less_count;
    }
};
```

## Method 2

Time Complexity: O(1)

Space Complexity: O(1)

```cpp
class Solution {
public:
    int minOperations(int n) {
        int remainder = n % 2;
        return (remainder + 1 + (n - 1)) * ((n - remainder) / 2) / 2;
    }
};
```


### Simplified Version

Runtime 0ms, Memory Usage 5.8MB.

Beat 100% in both time and space

```cpp
class Solution {
public:
    int minOperations(int n) {
        return (pow(n, 2) - pow(n % 2, 2)) / 4;
    }
};
```

Due to integer division, can be simplied to

```cpp
class Solution {
public:
    int minOperations(int n) {
        return pow(n, 2) / 4;
    }
};
```