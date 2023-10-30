# 682. Baseball Game

https://leetcode.com/problems/baseball-game/

Level: Easy

This is so easy so I won't explain. 

I just want to say,

1. Python is so slow
2. Java syntax is so hard

Same algorithm, Python version beats 13%, Java version beats 97%.


```python
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        for j in range(len(ops)):
            if ops[j] == "C":
                result.pop()
            elif ops[j] == "D":
                result.append(result[-1] * 2)
            elif ops[j] == "+":
                result.append(sum(result[-2:]))
            else:
                result.append(int(ops[j]))
        return sum(result)
```

```java
class Solution {
	/**
	 * Runtime: 2 ms, faster than 97.05% of Java online submissions for Baseball Game.
	 * Memory Usage: 40.6 MB, less than 88.72% of Java online submissions for Baseball Game.
	 */
    public int calPoints(String[] ops) {
        Stack<Integer> stack = new Stack();
        for(String op : ops) {
            if (op.equals("C")) {
                stack.pop();
            } else if (op.equals("D")) {
                stack.push(2 * stack.peek());
            } else if (op.equals("+")) {
                int top = stack.pop();
                int newtop = top + stack.peek();
                stack.push(top);
                stack.push(newtop);
            } else {
                stack.push(Integer.parseInt(op));
            }
        }
        int ans = 0;
        for(int score : stack) ans += score;
        return ans;
    }
}
```