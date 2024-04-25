import random
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return
    pivot_pos = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_pos]
    small = []
    large = []
    for i in range(0, len(arr)):
        if i != pivot_pos:
	        if arr[i] < pivot or arr[i] == pivot:
	            small.append(arr[i])
	        else:
	            large.append(arr[i])
            
    randomized_quick_sort(small)
    randomized_quick_sort(large)
    result = small + [pivot] + large
    arr[:] = result[:]
    
if __name__ == "__main__":
	arr = [3, 5, 1, 4, 2]
	randomized_quick_sort(arr)
	print(arr)
