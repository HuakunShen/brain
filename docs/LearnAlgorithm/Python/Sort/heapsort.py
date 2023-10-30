import isSorted
from DataStructure.maxHeap import *


def heap_sort(arr: list):
    hp = MaxHeap(arr)
    return hp.heap_sort()


isSorted.sorted_test(100, 100, heap_sort)
