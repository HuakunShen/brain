# 59. Spiral Matrix II

https://leetcode.com/problems/spiral-matrix-ii/

Level: Medium

## Solution

The difficulty of algorithm should be easy, it's just a little bit troublesome to handle all the cases.

There are not any tricky cases, but for each case you have to consider all scenarios carefully.

The input is a number $n$, and a board of $n \times n$ is generated, so I will say $N=n^2$

Time Comeplexity and Space complexity are both $O(N)$.

The space is allocated for a board of $n\times n$.

The time complexity comes from a single traverse of all the cells.

Although each step takes a lot of checks, it's still constant time.

4 variables `left`, `right`, `top`, `bottom` are defined to make the logic simpler, and save repetitive calculation.

The four variables mean whether the direction is available or empty (is 0).

With these varaibles, we know whether we are in corners.

### Input Cases

There are not many edge cases for inputs. 0 is not accepted. 

Try 1, 2, 3, 4, 5, which covers the smllest cases, even number and odd number.

### Movement Logic

There is not any specific algorithm used for this question, just simulate what a normal human would do, go in spirals.

There are 8 cases, 4 cases for each corner and 4 for each edge.

To simplify the 4 edge cases, we can simply define a `del_row` and a `del_col` indicating the 
direction of movement in both directions, because on edges, we just need to keep going in the same direction with 
momentum.

On the contrary, in corners you want to change the direction of movement by updating `del_row` and `del_col`.

The logic for each corner is commented in the code below.

The main logic is,

```
cur = 1
row, col = 0, 0
del_row, del_col = 0, 0
while there are space left:
	populate board at current position with value "cur"
	if on edges: keep moving in the same direction
	else if on corners: change the direction of movement
	
	row += del_row
	col += del_col
	cur += 1
```


```python
class Solution:
	# Runtime: 27 ms, faster than 97.24% of Python3 online submissions for Spiral Matrix II.
	# Memory Usage: 13.9 MB, less than 41.01% of Python3 online submissions for Spiral Matrix II.
	def generateMatrix(self, n: int) -> List[List[int]]:
		board = [[0 for i in range(n)] for j in range(n)]
		cur, del_row, del_col = 1, 0, 0
		r, c = 0, 0		# row and column (used a single letter to keep the code clean)
		while True:
			board[r][c] = cur
			left = c != 0 and board[r][c - 1] == 0
			right = c != n - 1 and board[r][c + 1] == 0
			top = r != 0 and board[r - 1][c] == 0
			bottom = r != n - 1 and board[r + 1][c] == 0
			# if top-left and empty right -> go right -> update del_row=0, del_col=1
			if not left and not top and right:
				del_row, del_col = 0, 1
			# elif top-right and empty bottom -> go down -> update del_row=1, del_col=0
			elif not left and not top and not right and bottom:
				del_row, del_col = 1, 0
			# elif bottom-right and empty left -> go down -> update del_row=0, del_col=-1
			elif not top and not right and not bottom and left:
				del_row, del_col = 0, -1
			# elif bottom-left and empty top -> go up -> update del_row=-1, del_col=0
			elif not bottom and not left and not right and top:
				del_row, del_col  = -1, 0
			# elif not corner and empty (0) in the next location, keep moving
			elif board[r + del_row][c + del_col] == 0:
				pass    
			# else, finished, verify that cur == n*n
			else:
				assert cur == n**2
				break
			r += del_row
			c += del_col
			cur += 1
		return board
```

## Zhuangbi Solution

```python
class Solution:
    """
    Runtime: 40 ms, faster than 68.74% of Python3 online submissions for Spiral Matrix II.
	Memory Usage: 13.9 MB, less than 85.81% of Python3 online submissions for Spiral Matrix II.
    """

    def generateMatrix(self, n: int) -> List[List[int]]:
        r, c, cur, del_row, del_col, board = 0, 0, 1, 0, 0, [[0 for __ in range(n)] for _ in range(n)]
        while True:
            left, right, top, bottom = c != 0 and board[r][c - 1] == 0, c != n - 1 and board[r][c + 1] == 0, r != 0 and board[r - 1][c] == 0, r != n - 1 and board[r + 1][c] == 0
            top_left, top_right, bottom_right, bottom_left = not left and not top and right, not left and not top and not right and bottom, not top and not right and not bottom and left, not bottom and not left and not right and top
            del_row, del_col = 0 if top_left or bottom_right else (1 if top_right else -1 if bottom_left else del_row), 0 if top_right or bottom_left else (1 if top_left else -1 if bottom_right else del_col)
            board[r][c] = cur
            if not((top_left and not top_right and not bottom_right and not bottom_left) or board[r + del_row][c + del_col] == 0): break
            r, c, cur = r + del_row, c + del_col, cur + 1
        return board
```


## Inside-out Solution

https://leetcode.com/problems/spiral-matrix-ii/discuss/22282

This person provides a 4-line solution in Python in a inside-out pattern.

Although it took advantage of many of Python's syntactic sugar, the inside-out solution is still super cool and elegant.

```bash

    ||  =>  |9|  =>  |8|      |6 7|      |4 5|      |1 2 3|
                     |9|  =>  |9 8|  =>  |9 6|  =>  |8 9 4|
                                         |8 7|      |7 6 5|
```

```python
# Build it inside-out
def generateMatrix(self, n):
    A, lo = [], n*n+1
    while lo > 1:
        lo, hi = lo - len(A), lo
        A = [range(lo, hi)] + zip(*A[::-1])
    return A

# Ugly inside-out
def generateMatrix(self, n):
    A = [[n*n]]
    while A[0][0] > 1:
        A = [range(A[0][0] - len(A), A[0][0])] + zip(*A[::-1])
    return A * (n>0)

# walk the spiral
def generateMatrix(self, n):
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in xrange(n*n):
        A[i][j] = k + 1
        if A[(i+di)%n][(j+dj)%n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A
```

See the [post](https://leetcode.com/problems/spiral-matrix-ii/discuss/22282) for detailed explanation. This 