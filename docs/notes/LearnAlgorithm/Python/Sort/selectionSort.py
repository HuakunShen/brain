import isSorted
import util

def selection_sort(arr):
	for i in range(len(arr)):
		smallest_index = util.find_smallest_index(arr, i, len(arr))
		util.swap(arr, i, smallest_index)
	

isSorted.sorted_test(100, 100, selection_sort)
