class Solution:
    def hammingWeight(self, n: int) -> int:

        cnt = 0

        # 1 =   1
        # 2 =  10
        # 3 =  11
        # 4 = 100

        while n:

            one_bit = n & 1
            if one_bit:
                cnt += 1
            n = n >> 1

        return cnt
        