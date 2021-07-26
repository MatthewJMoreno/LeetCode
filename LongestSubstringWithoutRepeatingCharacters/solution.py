"""
Given a string s, find the length of the longest substring without repeating characters.
"""
def lengthOfLongestSubstring(s):
  max_len = 0
  seen_chars = {}
  head = 0

  for i in range(len(s)):
    letter = s[i]

    if letter not in seen_chars:
      seen_chars[letter] = i
    else:
      head = max(head, seen_chars[letter] + 1)
      seen_chars[letter] = i
    
    max_len = max(max_len, i - head + 1)
  
  return max_len

test_1 = 'a'
test_2 = 'aaaa'
test_3 = 'abab'
test_4 = 'abcdabcde'
test_5 = 'abcdefg'
test_6 = 'aaadvdaqc'

print(lengthOfLongestSubstring(test_1))
print(lengthOfLongestSubstring(test_2))
print(lengthOfLongestSubstring(test_3))
print(lengthOfLongestSubstring(test_4))
print(lengthOfLongestSubstring(test_5))
print(lengthOfLongestSubstring(test_6))
