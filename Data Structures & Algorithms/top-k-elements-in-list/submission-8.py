class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        freqs = defaultdict(list)

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, freq in count.items():
            freqs[freq].append(num)

        for i in range(len(nums), -1, -1):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res

        