# 438. Find All Anagrams in a String

## Solution

### Using Python Counter Dict

```python
class Solution:
	"""
	Runtime: 569 ms, faster than 13.57% of Python3 online submissions for Find All Anagrams in a String.
	Memory Usage: 15.2 MB, less than 36.91% of Python3 online submissions for Find All Anagrams in a String.
	"""
    p1 = 0
    p2 = 0

    def findAnagrams(self, s: str, p: str) -> List[int]:
        count, n_s, n_p = Counter(p), len(s), len(p)
        if n_p > n_s:
            return []
        self.p1, self.p2 = 0, n_p - 1
        result = []
        window_count = Counter(filter(lambda x: x in count, s[self.p1:self.p2 + 1]))
        def run():
            if count == window_count:
                result.append(self.p1)
            if s[self.p1] in count:
                window_count[s[self.p1]] -= 1
            self.p1 += 1
            self.p2 += 1
            if self.p2 == n_s:
                return
            if s[self.p2] in count:
                window_count[s[self.p2]] += 1

        run()
        while self.p2 < n_s:
            run()
        return result
```

### Using Array (C++)

O(n) Time Complexity

```cpp
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int n_s = s.length();
        int n_p = p.length();
        if (n_s < n_p) return {};
        vector<int> freq_p(26, 0);
        vector<int> freq_window(26, 0);
        for(int i=0;i<n_p;i++){
            freq_p[p[i]-'a']++;
            freq_window[s[i]-'a']++;
        }
        vector<int> ans;
        if(freq_p == freq_window) ans.push_back(0);
        
        for(int i=n_p;i<n_s;i++){
            freq_window[s[i-n_p] - 'a']--;
            freq_window[s[i] - 'a']++;
            
            if(freq_p == freq_window) ans.push_back(i-n_p+1);
        }
        return ans;
    }
};
```