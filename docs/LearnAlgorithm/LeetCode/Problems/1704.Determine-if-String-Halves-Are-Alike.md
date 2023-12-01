# 1704. Determine if String Halves Are Alike

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

```python
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel_set = set(['a', 'e', 'i', 'o', 'u'])
        half1_count, half2_count = 0, 0
        for i in range(len(s)):
            if i < len(s) // 2:
                if s[i].lower() in vowel_set:
                    half1_count += 1
            else:
                if s[i].lower() in vowel_set:
                    half2_count += 1
        return half1_count == half2_count
```

```python
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        return (sum([1 for x in s[:len(s)//2] if x in vowels]) - sum([1 for x in s[len(s)//2:] if x in vowels])) == 0
```


```python
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l, m, s = len(s), len(s) // 2, s.lower()
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        n_vowel_a = sum([1 for x in s[:m] if x in vowels])
        n_vowel_b = sum([1 for x in s[m:] if x in vowels])
        return n_vowel_a == n_vowel_b
```