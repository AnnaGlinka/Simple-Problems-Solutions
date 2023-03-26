"""
https://leetcode.com/problems/happy-number/editorial/
https://leetcode.com/problems/happy-number/
 O(log⁡n)+O(log⁡log⁡n)+O(log⁡log⁡log⁡n)
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        sums_set = set()
        sum = 0
        while n:
            x = n % 10
            n //= 10
            sum += x*x
            if sum == 1 and n==0:
                return True
            if n == 0:
                if sum in sums_set:
                    return False
                sums_set.add(sum)
                n = sum
                sum = 0



s = Solution()
print(s.isHappy(19))
