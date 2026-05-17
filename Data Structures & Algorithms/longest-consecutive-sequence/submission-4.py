class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        longest = 0

        for n in num_set:                 # iterate once per unique number
            if n - 1 in num_set:          # skip if there’s a left neighbour
                continue

            cur_len = 1                   # count n itself
            cur = n
            while cur + 1 in num_set:     # walk to the right
                cur += 1
                cur_len += 1

            longest = max(longest, cur_len)

        return longest
