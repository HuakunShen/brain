#include <vector>
#include <set>
#include <iostream>
using namespace std;

class Solution {
public:
    /**
     * Runtime: 116 ms, faster than 19.03% of C++ online submissions for Contains Duplicate.
     * Memory Usage: 21 MB, less than 20.08% of C++ online submissions for Contains Duplicate.
     * @param nums
     * @return
     */
    bool containsDuplicate(vector<int>& nums) {
        set<int> s;
        for (int num: nums) {
            if (s.find(num) != s.end())
                return true;
            else
                s.insert(num);
        }
        return false;
    }
};

int main() {
    Solution sol;
    vector<int> nums{0};
    cout << sol.containsDuplicate(nums) << endl;
}