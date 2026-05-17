class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        visited = set()
        nums.sort()

        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:

                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum == 0 and (nums[i], nums[l], nums[r]) not in visited:
                    visited.add((nums[i], nums[l], nums[r]))
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif three_sum > 0:
                    r -= 1
                else:
                    l += 1
            
        return res

        