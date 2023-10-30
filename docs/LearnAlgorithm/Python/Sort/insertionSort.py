import isSorted
import util


def insertion_sort(arr: list):
    for i in range(len(arr)):
        smallest_index = util.find_smallest_index(arr, i, len(arr))
        if smallest_index != i:
            tmp_smallest_val = arr[smallest_index]
            shift(arr, i, smallest_index, 1)
            arr[i] = tmp_smallest_val


def shift(arr, index1, index2, num_shift):
    for i in range(index2 - 1, index1 - 1, -1):
        arr[i + num_shift] = arr[i]


isSorted.sorted_test(100, 100, insertion_sort)
