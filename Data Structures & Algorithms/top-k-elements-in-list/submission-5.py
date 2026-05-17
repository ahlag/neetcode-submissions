from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = defaultdict(list)
        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        for num, cnt in counts.items():
            freqs[cnt].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    return res





        