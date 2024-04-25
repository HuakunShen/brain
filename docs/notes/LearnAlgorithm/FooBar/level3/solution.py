"""
Each type of staircase should consist of 2 or more steps.
No two steps are allowed to be at the same height
each step must be lower than the previous one.
All steps must contain at least one brick. 
A step's height is classified as the total amount of bricks that make up that step.
"""
def solution(n):
	if n <= 4:
		return 1
	else:
		return solution(n - 1) + 1