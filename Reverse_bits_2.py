"""
https://leetcode.com/problems/reverse-bits/
https://www.youtube.com/watch?v=vy288ZcbWRc&t=269s
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1
            result = result | (n & 1)
            n >>= 1

        return result
    
        







