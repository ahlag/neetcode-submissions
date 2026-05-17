class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        integers = {}

        for i in range(len(nums)):

            diff = target - nums[i]
            print('idx:', i, 'diff:', diff, 'nums', integers)

            if diff in integers:
                return [integers[diff], i]
            
            integers[nums[i]] = i