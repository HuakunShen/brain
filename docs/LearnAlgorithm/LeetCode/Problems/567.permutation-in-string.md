# 567. Permutation in String

## Solutions

- [Official Solution](https://leetcode.com/problems/permutation-in-string/solutions/127729/short-permutation-in-a-long-string/)
- [Python Solution](https://leetcode.com/problems/permutation-in-string/solutions/1761953/python3-sliding-window-optimized-explained/)

## My Solution

I was using sliding window. It's very simple.

Set `l1 = len(s1)`, `l2 = len(s2)`.

The runtime is $\mathcal{O}(l_1+26*l_2)$.

The biggest bottlenect of my solution is the `s1counter == tracker` in every iteration. 
Causing the time to be multipled by at most 26, as every key in the counter dict may need to be checked. 

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1counter = Counter(s1)  # O(l1)
        tracker = Counter()
        for i, l in enumerate(s2): # l2 iterations
            tracker[l] += 1
            if i >= len(s1) and tracker[l] != 0:
                tracker[s2[i - len(s1)]] -= 1
            if s1counter == tracker:  # O(26)
                return True
        return False
```

## Optimized Solution

Although 26 is a constant, it's not the optimized solution. I am pretty sure there is a better solution that doesn't require such comparison in every iteration.

I think the optimized solution should use a method I would call "elimination" with a counter variable (integer). i.e. start from a s1 counter dict, eliminate elements in it as iterating through s2 str. When counter variable reaches 0, condition satisfied and we return True. But I didn't figure out how to do it.

My direction was right, similar to Approach 5 of the [Official Solution](https://leetcode.com/problems/permutation-in-string/solutions/127729/short-permutation-in-a-long-string/). 

The [Python Solution](https://leetcode.com/problems/permutation-in-string/solutions/1761953/python3-sliding-window-optimized-explained/) of the optimized solution is easier to understand, and is closer to my "elimination" method (not sure if it has a real name).


Here is the optimized solution.

The `match` is its counter variable. It monitors the number of matches .

This is also using sliding window in the for loop. Sliding window has a head and tail. 
The head takes in new element, and the tail pops one element out in every iteration. 

The `if s2[i] in cntr` is the head, and is doing the elimination process. 
When sliding window slides to the next position, it eats a new letter, decrement the `cntr[letter]` by one. 
When `cntr[letter]` is 0, that means this letter's count matches (i.e. the letters count in window matches the number of this letter in s1). 

The `not cntr[letter]` is actually checking `cntr[letter] == 0`.

The `if i >= w and s2[i-w] in cntr` is popping letter out. Increment `cntr[letter]` (0 means match).

Read comments for line-by-line explanation. 

Let's define "match for a letter" as, the number of of this letter in s1 is the same as the number of this letter in the sliding window.
Kind of like equilibrium, fluctuating around 0.


```python
def checkInclusion(self, s1: str, s2: str) -> bool:
	cntr, w, match = Counter(s1), len(s1), 0     

	for i in range(len(s2)):
		if s2[i] in cntr:  # sliding window takes a new letter
			if not cntr[s2[i]]: match -= 1  # current letter s2[i] already matches, getting another letter makes this letter unmatch
			cntr[s2[i]] -= 1                # eliminate the letter in cntr
			if not cntr[s2[i]]: match += 1  # cntr[s2[i]] was 1, then now, it becomes 0, reaches a match (equilibrium).

		if i >= w and s2[i-w] in cntr:  # sliding window popping a letter
			if not cntr[s2[i-w]]: match -= 1  # it's a match now, after popping a letter, match is broken for this letter
			cntr[s2[i-w]] += 1                # de-elimination of the popped letter, by incrementing the cntr[letter]
			if not cntr[s2[i-w]]: match += 1  # if equilibrium/match is reached after popping current letter, increment `match`

		if match == len(cntr):
			return True

	return False
```