# 1224. Maximum Equal Frequency

https://leetcode.com/problems/maximum-equal-frequency/

Level: hard

## Solution

### Initial Version, Timeout

```python
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        def default_count():
            return 0
        
        def works(count: Dict[int, int]):
            """Current state satisfy 'remove one and all counts are equal'"""
            count_2 = defaultdict(default_count)        # count of count, [1,2,2,3,3,4,4,4] -> count_2 = {1: 1, 2: 2, 3: 1}
            for num, count_ in count.items():
                count_2[count_] += 1
            count_2_closure = dict(count_2)
            count_2_values = list(count_2.values()) # count_2 = {2: 2, 3: 1} -> [2, 1]
            count_2_keys = list(count_2.keys()) # count_2 = {2: 2, 3: 1} -> [2, 3]
            if len(count_2) > 2:
                return False
            elif len(count_2) == 1:
                if count_2_values[0] == 1:
                    # target: [1, 1]
                    return True
                # True example: [1,2,3,4,5], [1]
                # False example: [1,1,2,2]
                return count_2_keys[0] == 1
            elif count_2[1] == 1:
                # special cases: 出现一次的有一个，那么把这1个删掉就好了。 如果出现一次的有2个，删掉其中一个
                # 例如：[1, 1, 2] -> count_2 = {1: 1, 2: 2}
                return True
            else:
                # 考虑删掉一个使它跟别的一样e.g. [2,2,3,3,4,4,4]
                if 1 not in count_2_values:
                    # 假设2个的次数是4，3个的次数是2， 那么肯定不行。2个的次数是4，3个的次数是1，把3个减掉变成2个，2个的次数就是5，就满足了
                    return False
                else:
                    # remove a number's occurrence by one, and its num occurrences is equal to all others
                    # count_2_rev[1] gives me the occurrence that appears only once
                    count_2_items = list(count_2_closure.items())
                    if count_2_items[0][0] - count_2_items[1][0] == 1 and count_2_items[0][1] == 1:
                        return True
                    if count_2_items[1][0] - count_2_items[0][0] == 1 and count_2_items[1][1] == 1:
                        return True
                    return False

        
        count = defaultdict(default_count)
        best_so_far = 0 # longest prefix so far
        
        for i in range(len(nums)):
            count[nums[i]] += 1
            if works(count):
                best_so_far = i + 1
        
        return best_so_far
```

## Solution 2 (Timeout)

This should be O(n), still timeouts.

A improved version of the previous version. Save time from removing for loop in `works` function which was used to 
recompute a hash map. The generation of the new hash map to store frequency of frequency types can be generated when 
the frequency hash map is being generated, so no need to 

```python
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        def default_count():
            return 0
        
        def non_0_dict(d: Dict):
            return {key: value for key, value in d.items() if value != 0}
        
        def non_0_len(d: Dict):
            return len([value for key, value in d.items() if value != 0])
        
        def works(count: Dict[int, int]):
            """Current state satisfy 'remove one and all counts are equal'"""
#             for num, count_ in count.items():
#                 count_2[count_] += 1
            count_2_closure = non_0_dict(count_2)
            count_2_values = list(count_2_closure.values()) # count_2 = {2: 2, 3: 1} -> [2, 1]
            count_2_keys = list(count_2_closure.keys()) # count_2 = {2: 2, 3: 1} -> [2, 3]
            if len(count_2_closure) > 2:
                # print("case 1")
                return False
            elif len(count_2_closure) == 1:
                # print("case 2")
                if count_2_values[0] == 1:
                    # target: [1, 1]
                    return True
                # True example: [1,2,3,4,5], [1]
                # False example: [1,1,2,2]
                return count_2_keys[0] == 1
            elif count_2[1] == 1:
                # print("case 3")
                # special cases: 出现一次的有一个，那么把这1个删掉就好了。 如果出现一次的有2个，删掉其中一个
                # 例如：[1, 1, 2] -> count_2 = {1: 1, 2: 2}
                return True
            else:
                # print("case 4")
                # 考虑删掉一个使它跟别的一样e.g. [2,2,3,3,4,4,4]
                if 1 not in count_2_values:
                    # 假设2个的次数是4，3个的次数是2， 那么肯定不行。2个的次数是4，3个的次数是1，把3个减掉变成2个，2个的次数就是5，就满足了
                    return False
                else:
                    # remove a number's occurrence by one, and its num occurrences is equal to all others
                    # count_2_rev[1] gives me the occurrence that appears only once
                    count_2_items = list(count_2_closure.items())
                    if count_2_items[0][0] - count_2_items[1][0] == 1 and count_2_items[0][1] == 1:
                        return True
                    if count_2_items[1][0] - count_2_items[0][0] == 1 and count_2_items[1][1] == 1:
                        return True
                    return False

        
        count = defaultdict(default_count)          # keeps track of frequency
        count_2 = defaultdict(default_count)        # count of count, [1,2,2,3,3,4,4,4] -> count_2 = {1: 1, 2: 2, 3: 1}
        best_so_far = 0 # longest prefix so far
        
        for i in range(len(nums)):
            count[nums[i]] += 1
            count_2[count[nums[i]]] += 1
            if count[nums[i]] != 1:
                count_2[count[nums[i]] - 1] -= 1
                # if count_2[count[nums[i]] - 1] == 0:
                #     count_2.pop(count[nums[i]])
                
            # print(count_2)
            if works(count):
                best_so_far = i + 1
        
        return best_so_far

```


## First Working Solution (Still Slow)

This is a improved version of the previous algorithm. `type_count` is now a global variable.

Save time converting between `defaultdict` and regular `dict`.

```python

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        def default_count():
            return 0

        def works():
            type_count_ = dict(type_count)
            type_count_keys = list(type_count_.keys())
            type_count_values = list(type_count_.values())
            if len(type_count_keys) > 2:
                return False
            elif len(type_count_keys) == 1:
                # [1], [1,2], [1,2,3], [1,1,2,2]
                if type_count_values[0] == 1:
                    # [1,1,1]
                    return True
                return type_count_keys[0] == 1  # [1,1,2,2] will fail, [1,2,3,4] will pass
            else:  # len(type_count_keys) == 2
                # e.g. [1,1,2,2,3]
                # e.g. [1,1,2,2,3,3,3]
                count_2_items = list(type_count_.items())  # O(1)
                if count_2_items[0][1] == 1:
                    if count_2_items[0][0] - count_2_items[1][0] == 1 or count_2_items[0][0] == 1:
                        return True
                elif count_2_items[1][1] == 1:
                    if count_2_items[1][0] - count_2_items[0][0] == 1 or count_2_items[1][0] == 1:
                        return True
                return False

        freq = defaultdict(default_count)  # keeps track of frequency
        type_count = defaultdict(default_count)  # count of count, [1,2,2,3,3,4,4,4] -> count_2 = {1: 1, 2: 2, 3: 1}
        best_so_far = 0  # longest prefix so far
        for i in range(len(nums)):
            freq[nums[i]] += 1
            type_count[freq[nums[i]]] += 1
            cur_freq = freq[nums[i]]
            if cur_freq != 1:
                # if current freq is 1, previous freq is 0, didn't exist, then no need to decrement type_count
                type_count[cur_freq - 1] -= 1  # decrement previous frequency type
                if type_count[cur_freq - 1] == 0:
                    type_count.pop(cur_freq - 1)
            if works():
                best_so_far = i + 1
        return best_so_far
```


### Another Way From Discussion

https://leetcode.com/problems/maximum-equal-frequency/discuss/1623255/Python-O(N)-time-comlexityorO(N)-space

The nature of this algorithm is pretty much the same as mine, but goes in another direction, making the algorithm much simpler.


Instead of computing and updating a best-so-far variable, this method goes backwards, pre compute a full hash map of 
frequency, starting from the end of array, stop when it sees the first solution. Very clever.

See [solution2.py](./solution2.py) for a modified version that's easier to understand.

## Test Cases

```
[1,1]
[1,2]
[1,1,1,2,2,2]
[2,2,1,1,5,3,3,5]
[1,1,1,2,2,2,3,3,3,4,4,4,5]
[1,2,3,4,5,6,7,8,9]
```

