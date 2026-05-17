class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [num for num in nums]
        has_zero = False
        zero_cnt = 0
        product = 1

        for i in range(n):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zero_cnt += 1
                
        if zero_cnt == 1:
            has_zero = True
        elif zero_cnt > 1:
            return [0] * n
        
        for i in range(n):
            if has_zero:
                if res[i] == 0:
                    res[i] = product
                else:
                    res[i] = 0
            else:
                res[i] = product // res[i]

        return res

        