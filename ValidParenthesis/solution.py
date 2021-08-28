'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

from collections import deque

class Solution:
  left_brackets = ['{', '[', '(']
  valid_pairs = ['()', f'{{}}', '[]']
  def __init__(self):
    self.left_brackets = ['{', '[', '(']
    self.valid_pairs = ['()', f'{{}}', '[]']
    
  def isValid(self, s):
    stack = deque()

    for bracket in s:
      if bracket in self.left_brackets:
        stack.append(bracket)
      elif len(stack) == 0:
        return False
      else:
        pair = '{}{}'.format(stack.pop(), bracket)
        if pair not in self.valid_pairs:
          return False
    
    if len(stack) == 0:
      return True
    
    return False

test_1 = f"[](){{}}"
test_2 = "]"
test_3 = "["
test_4 = "[(((){[]}))]"

solution = Solution()

print(solution.isValid(test_1))
print(solution.isValid(test_2))
print(solution.isValid(test_3))
print(solution.isValid(test_4))
