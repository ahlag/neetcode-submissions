class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Put all numbers into a set so we can check existence in O(1) time.
        digits = set(nums)
        longest = 0

        for num in nums:
            # Only start counting if num is the first number of a sequence.
            # If num - 1 exists, then num is in the middle of a sequence,
            # so we skip it to avoid repeated work.
            if num - 1 not in digits:
                cur_num = num
                cur_length = 1

                # Keep extending the sequence while the next number exists.
                while cur_num + 1 in digits:
                    cur_length += 1
                    cur_num = cur_num + 1
                # Update the longest sequence length found so far.
                longest = max(longest, cur_length)

        return longest
        