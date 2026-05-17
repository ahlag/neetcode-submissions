class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        digits = set(nums)
        longest = 0

        for num in nums:

            if num - 1 not in digits:
                cur_num = num
                cur_length = 1

                while cur_num + 1 in digits:
                    cur_length += 1
                    cur_num += 1
                
                longest = max(longest, cur_length)

        return longest
        