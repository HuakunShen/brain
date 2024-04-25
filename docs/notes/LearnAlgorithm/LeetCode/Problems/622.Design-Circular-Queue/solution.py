class MyCircularQueue:
    """Solution 0
    Runtime: 64 ms, faster than 90.02% of Python3 online submissions for Design Circular Queue.
    Memory Usage: 15 MB, less than 8.16% of Python3 online submissions for Design Circular Queue.
    """

    def __init__(self, k: int):
        self.queue = [0] * k
        self.size = k
        self.count = 0
        # beginning of queue (next element to be dequeued)
        self.start_cursor = 0
        self.end_cursor = 0         # position of next element

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.count += 1
        self.queue[self.end_cursor] = value
        self.end_cursor += 1
        if self.end_cursor == self.size:
            self.end_cursor = 0
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.count -= 1
        self.start_cursor += 1
        if self.start_cursor == self.size:
            self.start_cursor = 0
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.start_cursor]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        if self.end_cursor == 1:
            return self.queue[0]
        return self.queue[self.end_cursor - 1]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
