import heapq

class MedianFinder:

    def __init__(self):
        # min_heap stores the larger half of the numbers
        self.min_heap = []

        # max_heap stores the smaller half of the numbers
        # Python only supports min heaps, so we store negatives
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # First put the new number into max_heap
        # Store it as negative so it behaves like a max heap
        heapq.heappush(self.max_heap, -num)

        # Move the largest value from max_heap into min_heap
        # This keeps all values in max_heap <= all values in min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        # max_heap is allowed to have one more element than min_heap
        # If min_heap becomes bigger, move one back
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # If max_heap has one extra element,
        # its top is the median
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        
        