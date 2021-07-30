"""
Given a string s, return the longest palindromic substring in s.
"""

def find_longest_palindrome(s):
  palindrome_table = [[0 for y in range(len(s))] for x in range(len(s))]
  longest_palindrome_len = 0
  longest_palindrome = ''

  for i in range(len(s)):
    palindrome_table[i][i] = 1
    longest_palindrome = s[i]
    longest_palindrome_len = 1
  
  for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
      longest_palindrome = s[i:i+2]
      longest_palindrome_len = 2
      palindrome_table[i][i+1] = 1
  
  for substr_len in range(2, len(s)):
    for i in range(len(s)):
      if i + substr_len >= len(s):
        break

      is_palindrome = palindrome_table[i + 1][i + substr_len - 1]

      if s[i] == s[i + substr_len] and is_palindrome:
        if substr_len + 1 > longest_palindrome_len:
          longest_palindrome_len = substr_len + 1
          longest_palindrome = s[i: i + substr_len + 1]
        
        palindrome_table[i][i + substr_len] = 1
  
  return longest_palindrome

