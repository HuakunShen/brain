import math


def parent(i):
    return math.floor(i / 2)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


class MaxHeap:
    def __init__(self, data=None):
        if data:
            self.data = data
        else:
            self.data = []
        self.heap_size = 0

    def max_heapify(self, i):
        """
        When this method is called, assume the binary trees rooted at left(i) and right(i) are max-heaps
        :param i:
        :return:
        """
        l = left(i)
        r = right(i)
        if l < self.heap_size and self.data[l] > self.data[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.data[r] > self.data[largest]:
            largest = r
        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        """

        :return:
        """
        self.heap_size = len(self.data)
        for i in range(len(self.data) // 2 - 1, -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        """
        exchange the first(largest) element with the end of the data array
        reduce the heap size by one, assume the last element is gone
        and max-heapify the heap on root
        until last iteration, data[0] and data[1] are exchanged, the smallest element
        is left at position 0
        :return:
        """
        self.build_max_heap()
        for i in range(len(self.data) - 1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.heap_size -= 1
            self.max_heapify(0)
        return self.data

    def get_max(self):
        return self.data[0]

    def extract_max(self):
        if self.heap_size < 1:
            raise Exception("heap underflow")
        m = self.get_max()
        self.data[0] = self.data[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(0)
        return m

    def build_max_heap_2(self):
        self.heap_size = 0
        for i in range(0, len(self.data)):
            self.heap_insert(self.data[i])

    def increase_key(self, i, key):
        if key < self.data[i]:
            raise Exception("new key is smaller than current key")
        self.data[i] = key
        while i > 0 and self.data[parent(i)] < self.data[i]:  # while parent is smaller, swap
            self.data[i], self.data[parent(i)] = self.data[parent(i)], self.data[i]
            i = parent(i)

    def heap_insert(self, key):
        self.data[self.heap_size] = -float("inf")
        self.increase_key(self.heap_size, key)
        self.heap_size += 1

    def insert(self, key):
        self.data.append(-float("inf"))
        self.increase_key(self.heap_size, key)
        self.heap_size += 1


