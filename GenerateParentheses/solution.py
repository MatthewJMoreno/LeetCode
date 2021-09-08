"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
from typing import List, Optional

class Solution:
  def generate_parens_recursive(self, n, solution, parens, left_brackets, right_brackets):
    if len(parens) == n * 2:
      solution.append(parens)
      return
    
    if left_brackets < n:
      self.generate_parens_recursive(n, solution, parens + '(', left_brackets + 1, right_brackets)
    if right_brackets < left_brackets:
      self.generate_parens_recursive(n, solution, parens + ')', left_brackets, right_brackets + 1)

  def generateParenthesis(self, n: int) -> List[str]:
    solution = []
    self.generate_parens_recursive(n, solution, '', 0, 0)
    return solution

sol = Solution()
test = sol.generateParenthesis(3)
print(test)
