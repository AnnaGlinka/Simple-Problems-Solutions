"""
O(log n)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x !=0 ):
            return False

        start, stop = x, 0
        while start > stop:
            start, stop = start // 10, stop * 10 + start % 10

        return start == stop or start == stop // 10
        

s = Solution()
print(s.isPalindrome(12233221))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))