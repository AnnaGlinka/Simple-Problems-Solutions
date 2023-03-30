"""
https://leetcode.com/problems/reverse-bits/
https://www.youtube.com/watch?v=ZW7st_pN05w
https://towardsdatascience.com/understanding-bitmask-for-the-coding-interview-b1643f4b0e24
Turn the i^th bit to 1: mask = mask | (1 << i) , or mask |= (1 << i)
Flip the i^th bit: mask = mask ^ (1 << i) , or mask ^= (1 << i)
https://www.rapidtables.com/convert/number/hex-to-decimal.html
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        n = (n & 0xffff0000) >> 16 | (n & 0x0000ffff) << 16
        n = (n & 0xff00ff00) >> 8 | (n & 0x00ff00ff) << 8
        n = (n & 0xf0f0f0f0) >> 4 | (n & 0x0f0f0f0f) << 4
        n = (n & 0xcccccccc) >> 2 | (n & 0x33333333) << 2
        n = (n & 0xaaaaaaaa) >> 1 | (n & 0x55555555) << 1
        
        return n


# 0xffff0000 -> 11111111111111110000000000000000
# 0x0000ffff -> 1111111111111111
# 0xff00ff00 -> 11111111000000001111111100000000
# 0x00ff00ff -> 111111110000000011111111
# 0xf0f0f0f0 -> 11110000111100001111000011110000
# 0x0f0f0f0f -> 1111000011110000111100001111
# 0xcccccccc -> 11001100110011001100110011001100
# 0x33333333 -> 110011001100110011001100110011
# 0xaaaaaaaa -> 10101010101010101010101010101010
# 0x55555555 -> 1010101010101010101010101010101
        







