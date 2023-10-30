def swap(arr, index1, index2):
	arr[index1], arr[index2] = arr[index2], arr[index1]
	

def find_smallest_index(arr: list, start_index: int, end_index: int):
	smallest_index = start_index
	for i in range(start_index, end_index):
		if arr[smallest_index] > arr[i]:
			smallest_index = i
	return smallest_index
