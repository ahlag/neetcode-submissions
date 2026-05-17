class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        integers = {}

        for num in nums:

            if num not in integers:
                integers[num] = 1
            else:
                return True

        return False
