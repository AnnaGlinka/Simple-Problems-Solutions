"""
https://leetcode.com/problems/reverse-bits/
https://www.geeksforgeeks.org/reverse-bits-positive-integer-number-python/
https://www.youtube.com/watch?v=ZW7st_pN05w -> tutorial

https://realpython.com/python-bitwise-operators/

"""

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1
            if n&1 > 0: # n = n & 1
                result +=1
            n >>= 1

        return result
    
        







