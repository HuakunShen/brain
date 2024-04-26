# 775. Global and Local Inversions

[LeetCode Problem](https://leetcode.com/problems/global-and-local-inversions/submissions/)

## Brute Force

### Python Version
Timeout
```python
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        num_local, num_global = 0, 0
        for i in range(len(A)):
            if i < len(A) - 1 and A[i] > A[i + 1]:
                num_local += 1
            for j in range(i, len(A)):
                if A[i] > A[j]:
                    num_global += 1
        return num_local == num_global
```

### Golang Version
Runtime: 404 ms, faster than 15.38% of Go online submissions for Global and Local Inversions.
Memory Usage: 6.3 MB, less than 76.92% of Go online submissions for Global and Local Inversions.

```go
func isIdealPermutation(A []int) bool {
    num_local, num_global := 0, 0
    for i, v1 := range A {
        if i < len(A) - 1 && v1 > A[i + 1] {
            num_local += 1
        }
        for _, v2 := range A[i:] {
		    if v1 > v2 {
                num_global += 1
            }   
	    }
	}
    return num_local == num_global
}
```

## Math Solution
Runtime: 36 ms, faster than 96.88% of C++ online submissions for Global and Local Inversions.
Memory Usage: 35.7 MB, less than 24.11% of C++ online submissions for Global and Local Inversions.

### CPP Version
```cpp
class Solution {
public:
    bool isIdealPermutation(vector<int>& A) {
        for (int i = 0; i < A.size(); i++) {
            if (abs(A[i] - i) > 1)
                return false;
        }
        return true;
    }
};
```

### Python Oneliner
```python
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        return all(map(lambda x: abs(x[0] - x[1]) <= 1, enumerate(A)))
```

### Explanation

Each local inversion is also a global inversion, i.e. the given input should only contain local inversion.

**Then what is a global but not a local inversion?**

If 2 non-consecutive element are inversions, then there are at lease 2 global inversions.