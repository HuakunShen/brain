/**
Runtime: 4 ms, faster than 22.72% of C++ online submissions for Minimum Operations to Make Array Equal.
Memory Usage: 5.8 MB, less than 66.88% of C++ online submissions for Minimum Operations to Make Array Equal.
*/
class Solution0 {
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

class Solution1 {
public:
    int minOperations(int n) {
        int remainder = n % 2;
        return (remainder + 1 + (n - 1)) * ((n - remainder) / 2) / 2;
    }
};

class Solution2 {
public:
    int minOperations(int n) {
        return (pow(n, 2) - pow(n % 2, 2)) / 4;
    }
};

class Solution3 {
public:
    int minOperations(int n) {
        return pow(n, 2) / 4;
    }
};