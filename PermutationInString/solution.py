from typing import DefaultDict
import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = collections.defaultdict(int)
        for letter in s1: s1_dict[letter] += 1
        
        print(s1_dict)

        return True

sol = Solution()
s1 = 'aabs'
s2 = 'sqjfaabqjabsaj'

sol.checkInclusion(s1, s2)