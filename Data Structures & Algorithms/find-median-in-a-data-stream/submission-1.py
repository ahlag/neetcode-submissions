class MedianFinder:

    def __init__(self):
        self.array = []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.array.append(num)
        self.size += 1

    def findMedian(self) -> float:
        arr = sorted(self.array)
        n = self.size

        if n % 2:
            return arr[n//2]
        return (arr[n//2 - 1] + arr[n//2]) / 2
        
        