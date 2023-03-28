"""
https://leetcode.com/problems/isomorphic-strings/
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        from_to, to_from = {}, {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if (char_s in from_to and from_to[char_s] != char_t or 
                char_t in to_from and to_from[char_t] != char_s):
                return False
            from_to.update({char_s:char_t})
            to_from.update({char_t:char_s})

        return True



s = Solution()
#print(s.isIsomorphic("ege","add"))
print(s.isIsomorphic("badc","baba"))