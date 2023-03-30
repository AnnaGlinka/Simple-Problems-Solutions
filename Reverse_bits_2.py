"""
https://leetcode.com/problems/reverse-bits/
https://www.youtube.com/watch?v=vy288ZcbWRc&t=269s
https://realpython.com/python-bitwise-operators/
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1 #x2
            result = result | (n & 1)
            n >>= 1

        return result

s = Solution()
print(s.reverseBits(0xffffffff00000000))
        







