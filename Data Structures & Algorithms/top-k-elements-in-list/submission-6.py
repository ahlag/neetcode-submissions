class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []
        res = []
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        for freq, num in heap:
            res.append(num)

        return res

        