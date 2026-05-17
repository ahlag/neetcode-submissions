class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for n in numSet:

            # Check if the left neighbor exists
            if n - 1 in numSet:
                continue
            
            cur_len = 1
            cur = n

            while cur + 1 in numSet:
                cur = cur + 1
                cur_len += 1

            longest = max(longest, cur_len)

        return longest
