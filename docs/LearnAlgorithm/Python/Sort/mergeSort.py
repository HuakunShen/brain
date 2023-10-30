from isSorted import *
def merge_sort(arr: list):
	# Base Case
	if len(arr) <= 1:
		return
	# Divide
	mid = len(arr) // 2
	left = arr[:mid]
	right = arr[mid:]
	# Conquer
	merge_sort(left)
	merge_sort(right)
	# Combine (Generate) final solution
	merge(left, right, arr)


def merge(left: list, right: list, arr: list):
	i = j = num = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr[num] = left[i]
			i += 1
		else:
			arr[num] = right[j]
			j += 1
		num += 1
		
	if i < len(left):
		arr[num:] = left[i:]
	elif j < len(right):
		arr[num:] = right[j:]
	
if __name__ == "__main__":
	sorted_test(100, 100, merge_sort)
		
		
		
		
		
		
