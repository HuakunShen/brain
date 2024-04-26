import isSorted
import util
def bubble_sort(arr):
	if len(arr) <= 1:
		return

	for i in range(len(arr)):
		index1 = len(arr) - 2
		index2 = len(arr) - 1
		while index1 >= i:
			if arr[index1] > arr[index2]:
				util.swap(arr, index1, index2)
			index1 -= 1
			index2 -= 1


isSorted.sorted_test(100, 100, bubble_sort)


