class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0

        # 00...0100 -> 0010..00 
        # 0...    31 -> 31 ..  0

        for i in range(32):
            last_bit = (n >> i) & 1
            res |= (last_bit << (31 - i))

        return res


        
        