"""
https://leetcode.com/problems/reverse-bits/
https://www.youtube.com/watch?v=UcoN6UjAI64&t=603s
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << (31 - i))
        
        return result
    
        







