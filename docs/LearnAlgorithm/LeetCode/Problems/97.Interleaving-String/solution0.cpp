#include <iostream>
#include <cassert>
using namespace std;

class Solution0 {
public:
    bool isInterleave(string s1, string s2, string s3) {
        unsigned long sum_all = s1.length() + s2.length() + s3.length();
        if (sum_all == 0) {
            return true;
        } else if (sum_all != 0 && s3.length() == 0) {
            return false;
        } else {
            bool first_match = s1.length() && s1[0] == s3[0];
            bool second_match = s2.length() && s2[0] == s3[0];
            bool first_success = first_match ? this->isInterleave(s1.substr(1), s2, s3.substr(1)) : false;
            bool second_success = second_match ? this->isInterleave(s1, s2.substr(1), s3.substr(1)) : false;
            return first_success || second_success;
        }
    }
};

int main() {
    Solution0 sol;
    bool res = sol.isInterleave("aabcc", "dbbca", "aadbbbaccc");
    assert(res == 0);
    res = sol.isInterleave("abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb", "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc", "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc");
    assert(res == 1);
    res = sol.isInterleave("aabcc", "dbbca", "aadbbcbcac");
    assert(res == 1);
    return 0;
}