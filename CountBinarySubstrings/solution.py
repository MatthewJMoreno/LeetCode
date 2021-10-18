'''
Give a binary string s, return the number of non-empty substrings that have the same 
number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped 
consecutively.

Substrings that occur multiple times are counted the number of times they occur.

example: 1100101 has 5 substrings
'''

class Solution():
    def countBinarySubstrings(self, s: str) -> int:
        cur = 1
        prev = 0
        ans = 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                ans += min(cur, prev)
                prev = cur
                cur = 1
        
        return ans + min(cur, prev)
